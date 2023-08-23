from django.urls import path
from . import views


urlpatterns = [
    path('ingresar_evaluacion/', views.ingresar_evaluacion, name='ingresar_evaluacion'),
    path('lista_evaluaciones/', views.ResultadoEvaluacionListView.as_view(), name='lista_evaluaciones'),
]