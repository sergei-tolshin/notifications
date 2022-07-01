import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

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


class Template(TimeStampedFieldMixin, models.Model):
    # Шаблоны уведомлений
    # Доступно для менеджеров
    name = models.CharField(_('name'), max_length=200)
    notice = models.OneToOneField(
        Notice, on_delete=models.CASCADE,
        verbose_name=_('notice'),
        primary_key=True,
    )
    body = models.TextField(
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
