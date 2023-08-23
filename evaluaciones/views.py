from django.shortcuts import render, redirect
from .forms import ResultadoOFAForm, ResultadoEvaluacionForm
from  django.views.generic.list import ListView
from evaluaciones.models import ResultadoEvaluacion


def ingresar_evaluacion(request):
    if request.method =='POST':
        ofa_form = ResultadoOFAForm(request.POST)
        evaluacion_form = ResultadoEvaluacionForm(request.POST)
        if ofa_form.is_valid() and evaluacion_form.is_valid():
            ofa = ofa_form.save()
            evaluacion = evaluacion_form.save(commit=False)
            evaluacion.resultado_ofa = ofa
            evaluacion.save()

            return redirect('index')

    else:
        ofa_form = ResultadoOFAForm()
        evaluacion_form = ResultadoEvaluacionForm()

    context = {
        "ofa_form": ofa_form,
        "evaluacion_form": evaluacion_form,
    }

    return render(request, 'evaluaciones/ingresar_evaluacion.html', context)

class ResultadoEvaluacionListView(ListView):
    model = ResultadoEvaluacion
    template_name = "evaluaciones/lista_evaluaciones.html"