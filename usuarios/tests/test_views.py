import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Usuarios
from ..serializers import UserSerializer

client = Client()

class UsuariosConsultaTest(TestCase):
	# Teste para consulta de todos os usuários
	def setUp(self):
		Usuarios.objects.create(
			login='Casper', senha='123', data_nascimento='2003-07-05')
		Usuarios.objects.create(
			login='Muffin', senha='123', data_nascimento='2001-01-01')
		Usuarios.objects.create(
			login='Rambo', senha='123', data_nascimento='1958-07-02')
		Usuarios.objects.create(
			login='Ricky', senha='123', data_nascimento='2010-10-02')

	def test_consulta_usuarios(self):
		response = client.get(reverse('consulta_usuarios')+'?format=json')
		usuarios = Usuarios.objects.all()
		serializer = UserSerializer(usuarios, many=True)
		self.assertEqual(response.json(), serializer.data)

class UsuarioConsultaTest(TestCase):
	# Teste para consulta de um usuário
	def setUp(self):
		self.casper = Usuarios.objects.create(
			login='Casper', data_nascimento='2003-07-05')
		self.muffin = Usuarios.objects.create(
			login='Muffin', senha='123', data_nascimento='2001-01-01')
		self.rambo = Usuarios.objects.create(
			login='Rambo', senha='123', data_nascimento='1958-07-02')
		self.ricky = Usuarios.objects.create(
			login='Ricky', senha='123', data_nascimento='2010-10-02')

	def test_consulta_usuario_valido(self):
		response = client.get(reverse('consulta_usuario', kwargs={'pk': self.rambo.pk})+'?format=json')
		usuario = Usuarios.objects.get(pk=self.rambo.pk)
		serializer = UserSerializer(usuario)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_consulta_usuario_invalido(self):
		response = client.get(
			reverse('consulta_usuario', kwargs={'pk': 40}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CadastrarUsuarioTest(TestCase):
	# Teste para cadastrar usuários
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'senha': '123',
            'data_nascimento': '2000-01-01'
        }
        self.invalid_payload = {
            'name': '',
            'senha': '123',
            'data_nascimento': '2000-01-01'
        }

    def test_criar_usuario_valido(self):
        response = client.post(
            reverse('cadastrar_usuarios'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_criar_usuario_valido(self):
        response = client.post(
            reverse('cadastrar_usuarios'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)