from django.db import models
from django.contrib.auth.models import User

from .utils import senha_aleatoria

class Usuarios(models.Model):
	login = models.CharField(max_length=128)
	senha = models.CharField(max_length=128, default=User.objects.make_random_password(length=14))
	data_nascimento = models.DateField()