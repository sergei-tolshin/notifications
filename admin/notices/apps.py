from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NoticesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notices'
    verbose_name = _('notices')
