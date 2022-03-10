from django.urls import path
from helloworld.views import FuncionarioListView, FuncionarioDeleteView, FuncionarioCreateView

# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET/
    path('', views.index, name='index'),
    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
]
