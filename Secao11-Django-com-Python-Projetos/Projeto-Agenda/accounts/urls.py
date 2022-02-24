from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # ATENçÃO: --- ↑ - Não esquecer da barra!!!
    # Lembre-se que no: djAgPy\agendaContatos\urls.py
    # Também deve ter a barra no final.
]
