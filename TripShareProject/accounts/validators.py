from django.core.exceptions import ValidationError


def contains_only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Name must contain only letters.')
