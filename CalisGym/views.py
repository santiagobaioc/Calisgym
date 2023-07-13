from django.shortcuts import render
from CalisGym.models import Atleta, Entrenador, Competencia, Disciplina
from django.http import HttpResponse
from CalisGym.forms import DisciplinaFormulario, EntrenadorFormulario, AtletaFormulario, CompetenciaFormulario


# Create your views here.
def inicio(request):
    return render (request,"inicio.html")

def disciplinas(request):
      if request.method == "POST":
          miFormulario=DisciplinaFormulario(request.POST) 
          print(miFormulario)
          if miFormulario.is_valid():
              informacion = miFormulario.cleaned_data
              disciplina = Disciplina(nombre= informacion['nombre'],tipo=informacion['tipo'])
              disciplina.save()
              return render(request, 'inicio.html')
      else:
          miFormulario=DisciplinaFormulario()
      return render(request, "disciplinas.html",{"miFormulario":miFormulario})

def entrenadores(request):
    if request.method == "POST":
        miFormulario=EntrenadorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            entrenador=Entrenador(nombre=informacion['nombre'],apellido=informacion['apellido'],especialidad=informacion['especialidad'])
            entrenador.save()
            return render(request, 'inicio.html')
    else:
        miFormulario=EntrenadorFormulario()
    return render(request, 'entrenadores.html',{'miFormulario':miFormulario})

def atletas(request):
    if request.method == "POST":
        miFormulario=AtletaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            atleta=Atleta(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            atleta.save()
            return render (request, 'inicio.html')
    else:
        miFormulario=AtletaFormulario()
    return render (request, 'atletas.html',{'miFormulario':miFormulario})

def competencias(request):
    if request.method=="POST":
        miFormulario=CompetenciaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            competencia=Competencia(nombre=informacion['nombre'],fecha=informacion['fecha'],inscripcion=informacion['inscripcion'])
            competencia.save()
            return render (request, 'inicio.html')
    else:
        miFormulario=CompetenciaFormulario()
    return render(request, 'competencias.html',{'miFormulario':miFormulario})
    
            
def busquedaDisciplina(request):
    return render(request, 'busquedaDisciplina.html')
def buscar(request):
    if request.GET['camada']:

        tipo=request.GET['tipo']
        disciplina = Disciplina.objects.filter(tipo__icontains=tipo)
        return render(request, 'inicio.html',{'disciplinas':disciplina, 'tipo':tipo})
    else:
        respuesta= "No enviaste datos."
    
    #return HttpResponse(respuesta)
    return render (request, 'inicio.html',{'respuesta':respuesta})

def leerEntrenadores(request):
    entrenadores= Entrenador.objects.all()
    contexto={"entrenadores":entrenadores}
    return render (request, "leerEntrenadores.html", contexto)

def eliminarEntrenador(request, entrenador_nombre):
 
    entrenador = Entrenador.objects.get(nombre=entrenador_nombre)
    entrenador.delete()
 
    # vuelvo al menú
    entrenadores = Entrenador.objects.all()  # trae todos los entrenadores
 
    contexto = {"entrenadores": entrenadores}
 
    return render(request, "leerEntrenadores.html", contexto)

def editarEntrenador (request, entrenador_nombre):
    entrenador=Entrenador.objects.get(nombre=entrenador_nombre)
    if request.method == "POST":
        miFormulario=EntrenadorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            entrenador.nombre=informacion['nombre']
            entrenador.apellido=informacion['apellido']
            entrenador.especialidad=informacion['especialidad']

            entrenador.save()
            return render(request, 'inicio.html')
    else:
        miFormulario=EntrenadorFormulario(initial={'nombre':entrenador.nombre, 'apellido':entrenador.apellido, 'especialidad':entrenador.especialidad})
    return render(request, 'editarEntrenador.html',{'miFormulario':miFormulario, 'entrenador_nombre':entrenador_nombre})


