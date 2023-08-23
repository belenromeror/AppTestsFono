# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models


class Alumno(models.Model):
	nombres = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	fecha_nacimiento = models.DateField()
	curso = models.CharField(max_length=255) # Choices?

	def __str__(self):
		return self.nombres + " " + self.apellidos + " - " + self.curso

	def nombre_completo(self):
		return self.nombres + " " + self.apellidos

	def edad(self):
		hoy = datetime.now().date()
		return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
