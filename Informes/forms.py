from django import forms

class FormularioEstudiante(forms.Form):
    nombre_del_estudiante = forms.CharField(max_length=100)
    fecha_de_nacimiento = forms.DateField()
    edad= forms.CharField(max_length=100)
    fecha_informe = forms.DateField()

from django import forms

class FuncionesPrelinguisticasForm(forms.Form):
    RESPIRACION_CHOICES = [
        ('nasal', 'Nasal'),
        ('bucal', 'Bucal'),
        ('mixto', 'Mixto'),
    ]
    respiracion_modo = forms.ChoiceField(choices=RESPIRACION_CHOICES)

    TIPO_RESPIRACION_CHOICES = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    ]
    tipo_respiracion = forms.ChoiceField(choices=TIPO_RESPIRACION_CHOICES)

    TIPO_DEGLUCION_CHOICES = [
        ('normal', 'Normal'),
        ('atípica', 'Atípica'),
        ('interposición labio inferior', 'Interposicion labio inferior'),
        ('interposición lingual', 'Interposicion lingual'),
    ]
    tipo_deglucion = forms.ChoiceField(choices=TIPO_DEGLUCION_CHOICES)

    # Agrega mas campos de opciones y selecciones segun la informacion proporcionada
