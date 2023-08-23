from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('mostrar_informe/<int:pk>/', views.mostrar_informe, name='mostrar_informe'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
