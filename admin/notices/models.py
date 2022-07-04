import datetime as dt
import uuid

import pytz
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_celery_beat.models import PeriodicTask
from tinymce import models as tinymce_models

from .validators import validate_syntax


class DeliveryMethod(models.TextChoices):
    # Список методов(каналов) отправки уведомлений
    EMAIL = 'email', _('E-mail')
    SMS = 'sms', _('SMS')
    TELEGRAM = 'telegram', _('Telegram')
    WEBSOCKET = 'websocket', _('Websocket')


class UUIDFieldMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedFieldMixin(models.Model):
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class BaseModel(UUIDFieldMixin, TimeStampedFieldMixin):

    class Meta:
        abstract = True


class App(BaseModel):
    # Приложения, которые создают события
    # Доступ только для администраторов системы
    title = models.CharField(_('title'), max_length=200, unique=True,)
    name = models.CharField(_('name'), max_length=100, unique=True,)
    description = models.TextField(_('description'), blank=True, default='',)

    class Meta:
        db_table = "notice\".\"app"
        verbose_name = _('app')
        verbose_name_plural = _('apps')

    def __str__(self):
        return self.title


class Event(BaseModel):
    # События генерируемые приложниями
    # Доступ только для администраторов системы
    title = models.CharField(_('title'), max_length=200,)
    app = models.ForeignKey(App, on_delete=models.CASCADE,
                            verbose_name=_('app'), related_name='events',)
    name = models.CharField(_('name'), max_length=100,)
    description = models.TextField(_('description'), blank=True, default='',)

    class Meta:
        db_table = "notice\".\"event"
        unique_together = ('app', 'name')
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        return '{app}.{name}'.format(app=self.app.name, name=self.name)


class Notice(BaseModel):
    # Уведомления на созданные события
    # Доступ только для администраторов системы
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              verbose_name=_('event'),
                              related_name='notices')
    method = models.CharField(
        _('delivery method'),
        max_length=20,
        choices=DeliveryMethod.choices,
        default=DeliveryMethod.EMAIL,
    )
    controlled_by_user = models.BooleanField(
        verbose_name=_('controlled by user'),
        default=False
    )

    class Meta:
        db_table = "notice\".\"notice"
        unique_together = ('event', 'method')
        verbose_name = _('notice')
        verbose_name_plural = _('notices')

    def __str__(self):
        return '{event} | {method}'.format(event=self.event.title,
                                           method=self.get_method_display())


class Template(BaseModel):
    # Шаблоны уведомлений
    # Доступно для менеджеров
    name = models.CharField(_('name'), max_length=200)
    notice = models.ForeignKey(
        Notice, on_delete=models.CASCADE,
        verbose_name=_('notice'),
        related_name='templates',
    )
    by_default = models.BooleanField(
        verbose_name=_('by default for this notification'),
        default=False,
    )
    body = tinymce_models.HTMLField(
        _('message body'), blank=True,
        validators=[validate_syntax],
        help_text=_(
            "Allowed variables:<br>"
            "{{ name }} - user name<br>"
            "{{ login }} - user login<br>"
            "{{ email }} - user email<br>"
            "{{ code }} - activation code<br>"
            "{{ link }} - URL link"
        )
    )

    class Meta:
        db_table = "notice\".\"template"
        verbose_name = _('template')
        verbose_name_plural = _('templates')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        template = Template.objects.filter(notice=self.notice, by_default=True)
        if not self.by_default:
            if not template.exists():
                self.by_default = True
            return super().save(*args, **kwargs)
        with transaction.atomic():
            template.update(by_default=False)
            return super().save(*args, **kwargs)


class Newsletter(BaseModel):
    # Рассылки
    # Доступно для менеджеров
    title = models.CharField(_('title'), max_length=100,)
    subject = models.CharField(_('subject'), max_length=100,)
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE,
        verbose_name=_('template'),
        related_name='newsletters',
        limit_choices_to={'notice__event__app__name': 'promo'}
    )
    clocked_time = models.DateTimeField(
        verbose_name=_('clock time'),
        default=timezone.now,
        help_text=_('run the newsletter at the set time'),
    )

    def example_filter():
        return {
            "groups": ["subscription"],
            "age": ["gte=18", "lt=35"],
            "cities": ["Moscow", "Ekaterinburg"]
        }
    recipients = models.JSONField(
        verbose_name=_('recipients'),
        default=example_filter,
        help_text=_(
            'Example of a recipient filter:<br>'
            '{<br>'
            '&emsp;"groups": ["subscription"],<br>'
            '&emsp;"age": ["gte=18", "lt=35"],<br>'
            '&emsp;"cities": ["Moscow", "Ekaterinburg"]<br>'
            '}'
        )
    )
    task = models.OneToOneField(
        PeriodicTask,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    enabled = models.BooleanField(default=True, verbose_name=_('enabled'),)

    class Meta:
        db_table = "notice\".\"newsletter"
        verbose_name = _('newsletter')
        verbose_name_plural = _('newsletters')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.task is not None:
            self.task.delete()

        return super().delete(*args, **kwargs)


class UserNotice(BaseModel):
    # Настройки уведомлений, которые разрешил пользователь
    user_id = models.UUIDField(_('user id'))
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE,
                               verbose_name=_('notice'),
                               related_name='notices',
                               limit_choices_to={'controlled_by_user': True})

    class Meta:
        db_table = "notice\".\"user_notice"
        unique_together = ('user_id', 'notice')
        verbose_name = _('user notice')
        verbose_name_plural = _('user notices')


class UserTime(models.Model):
    # Часовой пояс и время получения уведомлений
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    HOUR_CHOICES = [
        (dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]

    user_id = models.UUIDField(_('user id'), primary_key=True)
    timezone = models.CharField(_('timezone'), max_length=32,
                                choices=TIMEZONES, default='UTC')
    time_from = models.TimeField(
        _('time from'), choices=HOUR_CHOICES, default=dt.time(00, 00))
    time_to = models.TimeField(
        _('time to'), choices=HOUR_CHOICES, default=dt.time(00, 00))

    class Meta:
        db_table = "notice\".\"user_time"
        verbose_name = _('user time')
        verbose_name_plural = _('user time')
