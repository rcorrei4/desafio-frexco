from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView

from .models import Usuarios
from .serializers import UserSerializer

class CriarUsuario(CreateAPIView):
    serializer_class = UserSerializer

class ConsultaUsuarios(ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer

class ConsultaUsuario(RetrieveAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer