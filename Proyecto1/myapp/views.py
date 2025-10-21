from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario, ProfesorFormulario
from django.db import models

def index(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/index.html', {'estudiantes': estudiantes})

def estudiantes(request):
    query = request.GET.get('q')  # Captura lo que se escribe en el buscador
    if query:
        estudiantes = Estudiante.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(email__icontains=query)
        )
    else:
        estudiantes = Estudiante.objects.all()

    return render(request, 'myapp/estudiantes_list.html', {
        'estudiantes': estudiantes,
        'query': query,
    })

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html',{'cursos': cursos})

def profesores(request):
    query = request.GET.get('q')  # Captura lo que se escribe en el buscador
    if query:
        profesores = Profesor.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(profesion__icontains=query)
        )
    else:
        profesores = Profesor.objects.all()


    return render(request, 'myapp/profesores.html', {
        'profesores': profesores,
        'query': query,
    })


def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html',{'entregables': entregables})

def cursoFormulario(request): 
    if request.method == 'POST': 
        form = CursoFormulario(request.POST) 
        if form.is_valid(): # Procesar los datos del formulario 
            nombre = form.cleaned_data['nombre'] 
            camada = form.cleaned_data['camada'] # Guardar los datos en la base de datos 
            curso = Curso(nombre=nombre, camada=camada) 
            curso.save() 
            return render(request, 'myapp/curso_exito.html') 
    else: 
        form = CursoFormulario() 
        
    return render(request, 'myapp/curso_formulario.html', {'form': form})

def profesorFormulario(request):
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesion = form.cleaned_data['profesion']

            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()
            return redirect('myapp:profesores')  # Redirige a la lista de profesores
    else:
        form = ProfesorFormulario()

    return render(request, 'myapp/profesor_formulario.html', {'form': form})
