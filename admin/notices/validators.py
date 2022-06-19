from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from jinja2 import Environment, TemplateSyntaxError, meta


def validate_syntax(value):
    allowed_vars = {'login', 'email', 'name'}
    try:
        env = Environment()
        t = env.parse(value)
        vars = meta.find_undeclared_variables(t)
        for var in vars:
            if var not in allowed_vars:
                raise ValidationError(
                    _("Variable '%(var)s' is forbidden"),
                    params={'var': var}
                )
    except TemplateSyntaxError as error:
        raise ValidationError(
            _("Syntax error: %(error)s"),
            params={'error': error}
        )
