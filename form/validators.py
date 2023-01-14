from django.core.exceptions import ValidationError

def nama_val(value):
    inputnama = value
    if inputnama == "Root":
        m = "Can't Input " + inputnama + " as Name!"
        raise ValidationError(m)