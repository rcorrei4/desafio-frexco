from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/usuarios/', views.CriarUsuario.as_view(), name='cadastrar_usuarios'),
    # Usar parâmetro format para escolher o tipo de arquivo para resposta (json, csv ou xlsx)
    path('consulta/usuarios/', views.ConsultaUsuarios.as_view(), name='consulta_usuarios'),
    path('consulta/usuario/<int:pk>/', views.ConsultaUsuario.as_view(), name='consulta_usuario')
]
