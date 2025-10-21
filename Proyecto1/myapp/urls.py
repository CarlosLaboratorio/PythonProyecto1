from django.urls import path
from . import views 

app_name = "myapp"
urlpatterns = [
    path("",views.index,name="index"),
    path('cursos/', views.cursos, name="cursos"), 
    path('profesores/', views.profesores, name="profesores"), 
    path('estudiantes/', views.estudiantes, name="estudiantes"), 
    path('entregables/', views.entregables, name="entregables"),
    path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    path('profesorFormulario/', views.profesorFormulario, name='profesorFormulario'),
    path('profesor/editar/<int:id>/', views.profesor_editar, name='profesorEditar'),
    path('profesor/eliminar/<int:id>/', views.profesor_eliminar, name='profesorEliminar'),
]
