from django import forms

from .models import ResultadoOFA, ResultadoEvaluacion


class ResultadoOFAForm(forms.ModelForm):
    mejillas = forms.MultipleChoiceField(
        choices=ResultadoOFA.OPCIONES_MEJILLAS,
        widget=forms.CheckboxSelectMultiple,
    )
    nariz = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_NARIZ,
        widget=forms.RadioSelect,
    )
    maxilar_inferior = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_MAXILAR_INFERIOR,
        widget=forms.RadioSelect,
    )
    fisura_labios = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FISURA_LABIOS,
        widget=forms.RadioSelect,
    )
    tamano_labios = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_TAMANO_LABIOS,
        widget=forms.RadioSelect,
    )
    funcionalidad_labios = forms.MultipleChoiceField(
        choices=ResultadoOFA.OPCIONES_FUNCIONALIDAD_LABIOS,
        widget=forms.CheckboxSelectMultiple,
    )
    funcionalidad_general_labios = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FUNCIONALIDAD_GENERAL_LABIOS,
        widget=forms.RadioSelect,
    )
    frenillo_labios = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FRENILLO_LABIOS,
        widget=forms.RadioSelect,
    )
    color_labios = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_COLOR_LABIOS,
        widget=forms.RadioSelect,
    )
    cierre_labial_reposo = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_CIERRE_LABIAL_REPOSO,
        widget=forms.RadioSelect,
    )
    cierre_labial_esfuerzo = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_CIERRE_LABIAL_ESFUERZO,
        widget=forms.RadioSelect,
    )
    tamano_lengua = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_TAMANO_LENGUA,
        widget=forms.RadioSelect,
    )
    frenillo_lengua = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FRENILLO_LENGUA,
        widget=forms.RadioSelect,
    )
    funcionalidad_lengua = forms.MultipleChoiceField(
        choices=ResultadoOFA.OPCIONES_FUNCIONALIDAD_LENGUA,
        widget=forms.CheckboxSelectMultiple,
    )
    funcionalidad_general_lengua = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FUNCIONALIDAD_GENERAL_LENGUA,
        widget=forms.RadioSelect,
    )
    forma_paladar_duro = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FORMA_PALADAR_DURO,
        widget=forms.RadioSelect,
    )
    fisura_paladar_duro = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FISURA_PALADAR_DURO,
        widget=forms.RadioSelect,
    )
    fistula_paladar_duro = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FISTULA_PALADAR_DURO,
        widget=forms.RadioSelect,
    )
    fisura_paladar_blando = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FISURA_PALADAR_BLANDO,
        widget=forms.RadioSelect,
    )
    movilidad_paladar_blando = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_MOVILIDAD_PALADAR_BLANDO,
        widget=forms.RadioSelect,
    )
    uvula = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_UVULA,
        widget=forms.RadioSelect,
    )
    tipo_uvula = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_TIPO_UVULA,
        widget=forms.RadioSelect,
    )
    amigdalas_palatinas = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_AMIGDALAS_PALATINAS,
        widget=forms.RadioSelect,
    )
    tamano_amigdalas_palatinas = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_TAMANO_AMIGDALAS_PALATINAS,
        widget=forms.RadioSelect,
    )
    etapa_denticion = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_ETAPA_DENTICION,
        widget=forms.RadioSelect,
    )
    arcada_superior = forms.MultipleChoiceField(
        choices=ResultadoOFA.OPCIONES_ARCADA_SUPERIOR,
        widget=forms.CheckboxSelectMultiple,
    )
    forma_arcada_superior = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_FORMA_ARCADA_SUPERIOR,
        widget=forms.RadioSelect,
    )
    arcada_inferior = forms.MultipleChoiceField(
        choices=ResultadoOFA.OPCIONES_ARCADA_INFERIOR,
        widget=forms.CheckboxSelectMultiple,
    )
    mordida_oclusion = forms.ChoiceField(
        choices=ResultadoOFA.OPCIONES_MORDIDA_OCLUSION,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = ResultadoOFA
        fields = "__all__"


class ResultadoEvaluacionForm(forms.ModelForm):
    fecha_evaluacion = forms.DateField(
        widget=forms.SelectDateWidget()
    )

    class Meta:
        model = ResultadoEvaluacion
        exclude = ["resultado_ofa", "id"]