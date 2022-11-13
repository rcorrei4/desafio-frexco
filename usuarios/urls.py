from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/', views.CriarUsuario.as_view(), name='cadastra_usuarios'),
    path('consulta/', views.ConsultaUsuarios.as_view(), name='consulta_usuarios'),
    path('consulta/usuario/<int:pk>/', views.ConsultaUsuario.as_view(), name='consulta_usuario')
]
