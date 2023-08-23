# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import ArrayField

from alumnos.models import Alumno


class ResultadoOFA(models.Model):
	OPCIONES_MEJILLAS = (
		("simetricas", "Simetricas"),
		("caidas", "Caidas"),
		("heridas_internas", "Heridas internas"),
	)

	OPCIONES_NARIZ = (
		("normal", "Normal"),
		("desviada", "Desviada"),
	)

	OPCIONES_MAXILAR_INFERIOR = (
		("normal", "Normal"),
		("micrognatia", "Micrognatia"),
		("prognatismo", "Prognatismo"),
	)

	OPCIONES_FISURA_LABIOS = (
		("si", "Si"),
		("no", "No"),
	)

	OPCIONES_TAMANO_LABIOS = (
		("normal", "Normal"),
		("evertido", "Evertido"),
		("corto", "Corto"),
	)

	OPCIONES_FUNCIONALIDAD_LABIOS = (
		("protusion", "Protusion"),
		("retrusion", "Retrusion"),
		("movimiento_lateral", "Movimiento lateral"),
		("vibracion", "Vibracion"),
	)

	OPCIONES_FUNCIONALIDAD_GENERAL_LABIOS = (
		("adecuada", "Adecuada"),
		("sin_movilidad", "Sin movilidad"),
		("disminuida", "Disminuida"),
	)

	OPCIONES_FRENILLO_LABIOS = (
		("normal", "Normal"),
		("corto", "Corto"),
	)

	OPCIONES_COLOR_LABIOS = (
		("normal", "Normal"),
		("secos", "Secos"),
		("rojos", "Rojos"),
	)

	OPCIONES_CIERRE_LABIAL_REPOSO = (
		("presente", "Presente"),
		("ausente", "Ausente"),
	)

	OPCIONES_CIERRE_LABIAL_ESFUERZO = (
		("presente", "Presente"),
		("ausente", "Ausente"),
	)

	OPCIONES_TAMANO_LENGUA = (
		("normal", "Normal"),
		("macroglosia", "Macroglosia"),
		("microglosia", "Microglosia"),
	)

	OPCIONES_FRENILLO_LENGUA = (
		("normal", "Normal"),
		("corto", "Corto"),
		("c_funcional", "C. funcional"),
		("grueso", "Grueso"),
		("anquilosante", "Anquilosante"),
	)

	OPCIONES_FUNCIONALIDAD_LENGUA = (
		("protusion", "Protusion"),
		("retrusion", "Retrusion"),
		("movimiento_lateral", "Movimiento lateral"),
		("elevacion", "Elevacion"),
		("adosamiento", "Adosamiento"),
		("chasquido", "Chasquido"),
	)

	OPCIONES_FUNCIONALIDAD_GENERAL_LENGUA = (
		("adecuada", "Adecuada"),
		("sin_movilidad", "Sin movilidad"),
		("disminuida", "Disminuida"),
	)

	OPCIONES_FORMA_PALADAR_DURO = (
		("normal", "Normal"),
		("ojival", "Ojival"),
		("otra", "Otra"),
	)

	OPCIONES_FISURA_PALADAR_DURO = (
		("si", "Si"),
		("no", "No"),
		("operada", "Operada"),
	)

	OPCIONES_FISTULA_PALADAR_DURO = (
		("si", "Si"),
		("no", "No"),
	)

	OPCIONES_FISURA_PALADAR_BLANDO = (
		("si", "Si"),
		("no", "No"),
		("operada", "Operada"),
	)

	OPCIONES_MOVILIDAD_PALADAR_BLANDO = (
		("adecuada", "Adecuada"),
		("sin_movilidad", "Sin movilidad"),
		("disminuida", "Disminuida"),
	)

	OPCIONES_UVULA = (
		("presente", "Presente"),
		("ausente", "Ausente"),
	)

	OPCIONES_TIPO_UVULA = (
		("normal", "Normal"),
		("corta", "Corta"),
		("larga", "Larga"),
		("bifida", "Bifida"),
	)

	OPCIONES_AMIGDALAS_PALATINAS = (
		("presente", "Presente"),
		("ausente", "Ausente"),
	)

	OPCIONES_TAMANO_AMIGDALAS_PALATINAS = (
		("normal", "Normal"),
		("aumentadas", "Aumentadas"),
		("disminuidas", "Disminuidas"),
		("asimetricas", "Asimetricas"),
	)

	OPCIONES_ETAPA_DENTICION = (
		("temporal", "Temporal"),
		("primera_fase", "Primera fase"),
		("segunda_fase", "Segunda fase"),
		("permanente", "Permanente"),
	)

	OPCIONES_ARCADA_SUPERIOR = (
		("mal_posiciones", "Mal posiciones"),
		("giroversiones", "Giroversiones"),
		("caries", "Caries"),
	)

	OPCIONES_FORMA_ARCADA_SUPERIOR = (
		("semicircular", "Semicircular"),
		("eliptica", "Eliptica"),
	)

	OPCIONES_ARCADA_INFERIOR = (
		("mal_posiciones", "Mal posiciones"),
		("giroversiones", "Giroversiones"),
		("caries", "Caries"),
	)

	OPCIONES_MORDIDA_OCLUSION = (
		("normal", "Normal"),
		("vis a vis", "Vis a vis"),
		("abierta", "Abierta"),
		("sobremordida", "Sobremordida"),
		("cruzada", "Cruzada"),
		("invertida", "Invertida"),
	)

	mejillas = ArrayField(
		models.CharField(max_length=255, choices=OPCIONES_MEJILLAS)
	)
	nariz = models.CharField(max_length=255, choices=OPCIONES_NARIZ)
	maxilar_inferior = models.CharField(max_length=255, choices=OPCIONES_MAXILAR_INFERIOR)

	# Labios
	fisura_labios = models.CharField(max_length=255, choices=OPCIONES_FISURA_LABIOS)
	tamano_labios = models.CharField(max_length=255, choices=OPCIONES_TAMANO_LABIOS)
	funcionalidad_labios = ArrayField(
		models.CharField(max_length=255, choices=OPCIONES_FUNCIONALIDAD_LABIOS)
	)
	funcionalidad_general_labios = models.CharField(max_length=255, choices=OPCIONES_FUNCIONALIDAD_GENERAL_LABIOS)
	frenillo_labios = models.CharField(max_length=255, choices=OPCIONES_FRENILLO_LABIOS)
	color_labios = models.CharField(max_length=255, choices=OPCIONES_COLOR_LABIOS)
	cierre_labial_reposo = models.CharField(max_length=255, choices=OPCIONES_CIERRE_LABIAL_REPOSO)
	cierre_labial_esfuerzo = models.CharField(max_length=255, choices=OPCIONES_CIERRE_LABIAL_ESFUERZO)

	# Lengua
	tamano_lengua = models.CharField(max_length=255, choices=OPCIONES_TAMANO_LENGUA)
	frenillo_lengua = models.CharField(max_length=255, choices=OPCIONES_FRENILLO_LENGUA)
	funcionalidad_lengua = ArrayField(
		models.CharField(max_length=255, choices=OPCIONES_FUNCIONALIDAD_LENGUA)
	)
	funcionalidad_general_lengua = models.CharField(max_length=255, choices=OPCIONES_FUNCIONALIDAD_GENERAL_LENGUA)

	# Paladar duro
	forma_paladar_duro = models.CharField(max_length=255, choices=OPCIONES_FORMA_PALADAR_DURO)
	fisura_paladar_duro = models.CharField(max_length=255, choices=OPCIONES_FISURA_PALADAR_DURO)
	fistula_paladar_duro = models.CharField(max_length=255, choices=OPCIONES_FISTULA_PALADAR_DURO)

	# Paladar blando
	fisura_paladar_blando = models.CharField(max_length=255, choices=OPCIONES_FISURA_PALADAR_BLANDO)
	movilidad_paladar_blando = models.CharField(max_length=255, choices=OPCIONES_MOVILIDAD_PALADAR_BLANDO)

	uvula = models.CharField(max_length=255, choices=OPCIONES_UVULA)
	tipo_uvula = models.CharField(max_length=255, choices=OPCIONES_TIPO_UVULA)
	amigdalas_palatinas = models.CharField(max_length=255, choices=OPCIONES_AMIGDALAS_PALATINAS)
	tamano_amigdalas_palatinas = models.CharField(max_length=255, choices=OPCIONES_TAMANO_AMIGDALAS_PALATINAS)
	etapa_denticion = models.CharField(max_length=255, choices=OPCIONES_ETAPA_DENTICION)
	arcada_superior = ArrayField(
		models.CharField(max_length=255, choices=OPCIONES_ARCADA_SUPERIOR)
	)
	forma_arcada_superior = models.CharField(max_length=255, choices=OPCIONES_FORMA_ARCADA_SUPERIOR)
	arcada_inferior = ArrayField(
		models.CharField(max_length=255, choices=OPCIONES_ARCADA_INFERIOR)
	)
	mordida_oclusion = models.CharField(max_length=255, choices=OPCIONES_MORDIDA_OCLUSION)


"""
class ResultadoAntecedentesPragmaticos(models.Model):
	contacto_visual = models.BooleanField()
	(otros campos)
"""
	

class ResultadoEvaluacion(models.Model):
	alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
	fecha_evaluacion = models.DateTimeField()
	resultado_teprosif = models.IntegerField()
	resultado_stsg_e = models.IntegerField()
	resultado_stsg_r = models.IntegerField()
	resultado_tecal = models.IntegerField()

	resultado_ofa = models.OneToOneField(ResultadoOFA, on_delete=models.CASCADE)
	# resultado_antecedentes_pragmaticos = models.OneToOneField(ResultadoAntecedentesPragmaticos, on_delete=models.CASCADE)
