from django.core.exceptions import ValidationError

def value_is_lowercase(value):
    if value != value.lower():
        value = value.lower()
        return value_is_lowercase(value)
    return value

def value_is_already_exists(value):
    try:
        from Personal.models import Puestos
        puesto = Puestos.objects.get(Puesto = value)
    except:
        puesto = None

    if puesto:
        raise ValidationError('EL puesto ya existe')

    return value

def value_exists(value):
    try:
        from Personal.models import Puestos
        puesto = Puestos.objects.get(Puesto = value.lower())
    except:
        puesto = None

    if puesto == None:
        raise ValidationError('Este puesto no existe')
    return value

def value_is_number(value):
    new_value = value
    try:
        new_value = int(value)
    except:
        pass
    if type(new_value) != int:
        raise ValidationError('El centro de costo tiene que ser un número')
    return value

def value_area_is_already_exists(value):
    try:
        from Personal.models import Areas
        area = Areas.objects.get(Area = value.lower())
    except:
        area = None

    if area:
        raise ValidationError('EL area ya existe')

    return value

def value_cdc_is_already_exists(value):
    try:
        from Personal.models import Areas
        area = Areas.objects.get(CDC = value)
    except:
        area = None

    if area:
        raise ValidationError('EL Centro de costo ya existe')

    return value

def value_exists_area(value):
    new_cdc = False
    new_area = False
    try:
        from Personal.models import Areas
        new_area = Areas.objects.filter(Area = value.lower()) or False
    except:
        pass

    try:
        from Personal.models import Areas
        new_cdc = Areas.objects.filter(CDC = int(value)) or False
    except:
        pass
    if new_area == False and new_cdc == False:
        raise ValidationError('Esta area no existe')
    return value
