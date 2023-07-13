from django import forms
 
class DisciplinaFormulario(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()

class EntrenadorFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    especialidad=forms.CharField()
    
class AtletaFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()

class CompetenciaFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    fecha=forms.DateField()
    inscripcion=forms.BooleanField()