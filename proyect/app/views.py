
# Create your views here.
from lib2to3.pgen2 import token
from urllib import response
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password,check_password
import numpy
from .models import Nivel, User
from cryptography.fernet import Fernet

key = 'edSwgzGBesPsxxY2UGnBPrZdypNEedQbMY70JXvBWKQ=tnIrmHjyCSsO7WYlSbDF'
token =  key

def authenticate(request):
    if request.method == 'POST':
        web_token = request.POST.get('web_token')
        if web_token == token.decode():
            return True
    return False

def login (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = list(User.objects.filter(email = email).values())
        if(len(user)>0):
            bool = check_password(password=password,encoded=user[0]['password'])
            if bool:
                data = {
                    'Message':'Inicio de sesion',
                    'Color': 'green',
                    'Status': 1,
                    'Token': user[0]['token_user']
                    }
            else: 
                data = {
                    'Message': 'Contraseña incorrecta',
                    'Color': 'red',
                    'Status': -1
                }
        else:
            data = {
                'Message': 'No se ha encontrado el usuario',
                'Color': 'red',
                'Status': -1
            }
        return JsonResponse(data)

def register (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        user = list(User.objects.filter(email=email).values())
        user_token = make_password(key)
        if len(user)>0:
            response = {
                    'Message':'El correo ya está registrado',
                    'Color': 'red',
                    'Status': -1
                }
        else:
            User.objects.create(
                email = email,
                password = hashed_password,
                user_type = 1,
                token_user = user_token
            )
            response = {
                'Message':'Usuario registrado exitosamente',
                'Color': 'green',
                'Status': 1,
            }
    return JsonResponse(response)

def verifyToken(request):
    if request.method == 'POST':
        web_token = request.POST.get('web_token')
        token = list(User.objects.filter(token_user=web_token).values())
        if(web_token == token[0]['token_user']):
            response = {
                'Message': 'El token ha sido verificado',
                'Status': 1
            }
        else:
            response = {
                'Message':'El token es incorrecto',
                'Status': -1
            }
    return JsonResponse(response)

def niveles (request,id=0):
    if request.method == 'POST':
        if id == 0:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            nivel = list(Nivel.objects.filter(nombre=nombre).values())
            if len(nivel)>0:
                response = {
                    'Message': 'El nivel ya existe',
                    'Color': 'red',
                    'Status':-1
                }
            else:
                Nivel.objects.create(
                    nombre = nombre,
                    descripcion = descripcion
                )
                response = {
                    'Message':'Nivel creado exitosamente',
                    'Color':'green',
                    'Status': 1
                }
        else: 
            niveles = list(Nivel.objects.filter(id=id).values())
            if len(niveles)>0:
                nivel = Nivel.objects.get(id=id)
                nivel.nombre = request.POST.get('nombre')
                nivel.descripcion = request.POST.get('descripcion')
                nivel.save()
                response = {
                    'Message': 'El nivel se ha actualizado',
                    'Color': 'green',
                    'Status': 1
                }
            else:
                response = {
                    'Message': 'No se encontró el nivel',
                    'Color': 'red',
                    'Status': -1
                }
    if request.method == 'GET':
        if id > 0:
            nivel = list(Nivel.objects.filter(id=id).values())
            if len(nivel)>0:
                response = {
                    'Message': 'Se encontró el nivel',
                    'Color':'green',
                    'Status':1
                }
            else: 
                response = {
                    'Message':'No se encontró el nivel',
                    'Color': 'red',
                    'Status': -1
                }
        else:
            niveles = list(Nivel.objects.all().values())
            response = {
                'Data': niveles
            }
    if request.method == 'DELETE':
        nivel = list(Nivel.objects.filter(id=id))
        if len(nivel)>0:
            Nivel.objects.filter(id=id).delete()
            response = {
                'Message': 'Se eliminó el nivel',
                'Color': 'green',
                'Status': 1
            }
        else: 
            response = {
                'Message': 'No se encontró el nivel',
                'Color': 'red',
                'Status': -1
            }
    return JsonResponse(response)