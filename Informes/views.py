import statistics
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from evaluaciones.models import ResultadoEvaluacion


def mostrar_informe(request, *args, **kwargs):
    evaluacion_id = kwargs.get("pk")
    try:
        evaluacion = ResultadoEvaluacion.objects.get(id=evaluacion_id)
    except ResultadoEvaluacion.DoesNotExist:
        return HttpResponseNotFound()

    fecha = request.GET.get("fecha", evaluacion.fecha_evaluacion.strftime("%d-%m-%Y"))

    queryset_evaluaciones = ResultadoEvaluacion.objects.all()
    calcular_stdev = queryset_evaluaciones.count()>1
    
    context = {
        "resultado_evaluacion": {
            "teprosif": {
                "total": evaluacion.resultado_teprosif,
                "desv_estandar": statistics.stdev(
                    queryset_evaluaciones.values_list("resultado_teprosif", flat=True)
                )
                if calcular_stdev else 0

            }, "stsg_r": {
                "total": evaluacion.resultado_stsg_r,
                "desv_estandar": statistics.stdev(
                    queryset_evaluaciones.values_list("resultado_stsg_r", flat=True)
                )
                if calcular_stdev else 0
            }, "stsg_e": {
                "total": evaluacion.resultado_stsg_e,
                "desv_estandar": statistics.stdev(
                    queryset_evaluaciones.values_list("resultado_stsg_e", flat=True)
                )
                if calcular_stdev else 0
            }, "tecal": {
                "total": evaluacion.resultado_tecal,
                "desv_estandar": statistics.stdev(
                    queryset_evaluaciones.values_list("resultado_tecal", flat=True)
                )
                if calcular_stdev else 0
            }
        }, 
        "fecha_evaluacion": fecha,
        "alumno": evaluacion.alumno
    }

    return render(request, 'informe.html', context)
