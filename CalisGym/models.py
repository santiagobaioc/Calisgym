from django.db import models

# Create your models here.
class Disciplina(models.Model):
    nombre=models.CharField(max_length=40)
    tipo=models.CharField(max_length=40)

    
class Atleta(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Entrenador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    especialidad=models.CharField(max_length=30)
   

class Competencia(models.Model):
    nombre= models.CharField(max_length=30)
    fecha=models.DateField()
    inscripcion=models.BooleanField()