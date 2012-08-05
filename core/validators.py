from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
import re

def UsernameValidator(value):
    pattern = re.compile(" ")
    if not pattern.search(value) == None:
        raise ValidationError(_(u'O nome de usuario nao pode conter espacos'))

def PasswordValidator(value):
    if len(value) < 4:
        raise ValidationError(_(u'A senha deve ter 4 digitos no minimo'))