# Instalando ambiente virtual
python3 -m venv venv

# Ativando e desativando ambiente virtual
. venv/bin/activate

deactivate

# Instalando django no ambiente virtual
pip install django

# Iniciando project django
django-admin startproject project .

# Rodando django-admin
python manage.py runserver

# Migrando a base de dados do Django
python manage.py makemigrations
python manage.py migrate

# Criando e modificando a senha de um super usuário
python manage.py createsuperuser
python manage.py changepassword USERNAME

# criando app
python manage.py startapp contact

# Instalando Django Rest Framework
pip install djangorestframework markdown django-filter

pip freeze > requirements.txt

# arquivos estáticos
python manage.py collectstatic

# executando o script de dados fakes
python utils/create_contacts.py

# Configure o .gitignore
# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT


# Monstrando o models e serializer no shell
export DJANGO_SETTINGS_MODULE=project.settings

import django
django.setup()
from rest_framework.renderers import JSONRenderer
from cursos.models import Curso
from cursos.serializers import CursoSerializer
curso = Curso.objects.latest('id')
curso
curso.titulo
serializer = CursoSerializer(curso)
serializer
serializer.data
JSONRenderer().render(serializer.data)

# Criando token através do shell
export DJANGO_SETTINGS_MODULE=project.settings

import django
django.setup()
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
user = User.objects.get(id=1)
user.email
user.username
token = Token.objects.create(user=user)
token.key
