from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class SpecialCharacterValidator():

    special_characters = "@#$%&_+{}"

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(char in SpecialCharacterValidator.special_characters for char in password):
            raise ValidationError(_(f'Password must contain at least {self.min_length} special character from this list: {SpecialCharacterValidator.special_characters}'))

    def get_help_text(self):
        return f'Your password must contain at least {self.min_length} special character from this list: {SpecialCharacterValidator.special_characters}'


class UppercaseValidator():
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError(_(f'Password must contain at least {self.min_length} uppercase letter'))

    def get_help_text(self):
        return f'Your password must contain at least {self.min_length} uppercase letter'


class DigitValidator():
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(_(f'Password must contain at least {self.min_length} digit'))

    def get_help_text(self):
        return f'Your Password must contain at least {self.min_length} digit'
