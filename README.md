# Desafio Tech (Automação) Frexco - API Django

## Instalação
Instalar dependências:
```
pip install -r requirements.txt
```
Inicializar o banco de dados:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Iniciar o servidor:
```
python3 manage.py runserver
```

## API Endpoints
### Consultar usuários - GET
```
/api/consulta/usuarios/
```
Parâmetros da URL:
- format
	- json
	- xlsx
	- csv

Exemplo:
```
/api/consulta/usuarios/?format=xlsx
```
### Consultar usuário - GET
```
/api/consulta/usuario/{id_usuario}/
```
### Cadastrar usuário - POST
```
/api/cadastrar/usuarios/
```
Campos:
- login -> char
- senha -> char
- data_nascimento -> date (DD-MM-AAAA)