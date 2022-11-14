from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Usuarios

erro_senha = {
	"blank": "A senha não pode ficar em branco (caso não queira colocar a senha apenas não a envie)",
}

erros = {
	"required": "Este campo é necessário!",
	"blank": "Este campo não pode ficar vazio!",
	"null": "Este campo não pode ser nulo!",
	"date_x": "Formatação inválida! (AAAA-MM-DD)"
}


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuarios
		fields = '__all__'
		extra_kwargs = {
			"login": {"error_messages": erros},
			"senha": {"error_messages": erro_senha},
			"data_nascimento": {"error_messages": erros}
		}