import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_syntax


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


class DeliveryMethod(models.TextChoices):
    EMAIL = 'email', _('E-mail')
    SMS = 'sms', _('SMS')
    TELEGRAM = 'telegram', _('Telegram')
    WEBSOCKET = 'websocket', _('Websocket')


class Template(BaseModel):
    method = models.CharField(
        _('delivery method'),
        max_length=20,
        choices=DeliveryMethod.choices,
        default=DeliveryMethod.EMAIL,
    )
    name = models.CharField(_('name'), max_length=200, unique=True,)
    body = models.TextField(
        _('message body'), blank=True,
        validators=[validate_syntax],
        help_text=_(
            "Allowed variables:<br>"
            "{{ name }} - user name<br>"
            "{{ login }} - user login<br>"
            "{{ email }} - user email"
        )
    )

    class Meta:
        db_table = "notice\".\"template"
        verbose_name = _('template')
        verbose_name_plural = _('templates')

    def __str__(self):
        return self.name
