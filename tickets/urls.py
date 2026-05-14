from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('cine/', views.cine, name="cine"),
    path('tickets/', views.tickets, name="tickets"),
    path('metodos/', views.lista_metodos_pago, name="lista_metodos"),
    path('metodos/crear', views.crear_metodo_pago, name="crear_metodo_pago"),
    path('metodos/editar/<int:id>/', views.editar_metodo, name="editar_metodo"),
    path('metodos/borrar/<int:id>/', views.borrar_metodo, name="borrar_metodo"),
]