from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_pandas import PandasView

from .models import Usuarios
from .serializers import UserSerializer

class CriarUsuario(CreateAPIView):
    serializer_class = UserSerializer

class ConsultaUsuarios(PandasView, ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer

class ConsultaUsuario(PandasView, RetrieveAPIView):
    queryset = Usuarios.objects.filter()
    serializer_class = UserSerializer