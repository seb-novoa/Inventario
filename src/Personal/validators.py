from django.core.exceptions import ValidationError
def value_is_lowercase(value):
    if value != value.lower():
        value = value.lower()
        return value_is_lowercase(value)
    return value
