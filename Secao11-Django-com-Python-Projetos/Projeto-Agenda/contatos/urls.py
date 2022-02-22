from django.urls import path
from . import views

# Como exibir nome ao invez da Id na barra de endereços? -----------------------------

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),  # modifique aqui
]
