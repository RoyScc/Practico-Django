from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cine/', views.cine, name="cine"),
    path('carreras/', views.carreras, name="carreras"),
    path('shows/', views.shows, name="shows"),
]