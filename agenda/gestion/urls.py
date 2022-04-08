from django.urls import path
from .views import inicio, PruebaApiView, TareasApiView, EtiquetasApiView

urlpatterns = [
    path('inicio', inicio),
    path('prueba', PruebaApiView.as_view()),
    path('tareas', TareasApiView.as_view()),
    path('etiquetas', EtiquetasApiView.as_view()),
]
































