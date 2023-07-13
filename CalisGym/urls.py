from django.urls import path
from CalisGym import views


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('disciplinas', views.disciplinas, name="Disciplinas"),
    path('entrenadores', views.entrenadores, name="Entrenadores"),
    path('atletas', views.atletas, name="Atletas"),
    path('competencias', views.competencias, name="Competencias"),
    path('busquedaDisciplina',views.busquedaDisciplina, name='BusquedaDisciplina'),
    path('buscar',views.buscar),
    path("leerEntrenadores", views.leerEntrenadores, name="LeerEntrenadores"),
    path("eliminarEntrenador/<entrenador_nombre>", views.eliminarEntrenador, name="EliminarEntrenador"),
    path('editarEntrenador/<entrenador_nombre>/', views.editarEntrenador, name='EditarEntrenador'),
    
]