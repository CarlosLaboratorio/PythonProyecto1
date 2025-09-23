from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario 

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
    return render(request, 'myapp/profesores.html',{'profesores': profesores})

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