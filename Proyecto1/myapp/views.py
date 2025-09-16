from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

def index(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/index.html', {'estudiantes': estudiantes})

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html',{'cursos': cursos})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, '',{'profesores': profesores})

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, '',{'entregables': entregables})
