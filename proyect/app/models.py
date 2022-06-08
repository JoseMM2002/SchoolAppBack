from datetime import date
from django.db import models
# Create your models here.
class Nivel(models.Model):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    created_at = date.today().strftime("%d/%m/%Y %H:%M:%S")

class User(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    user_type = models.IntegerField(default=1)
    token_user = models.CharField(max_length=100)

class UserData(models.Model):
    def __init__(self):
        super().__init__()
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    appelidoP = models.CharField(max_length=50)
    appelidoM = models.CharField(max_length=50)
    nivel = models.OneToOneField(Nivel,null=True,on_delete=models.CASCADE)


class Materia(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    nivel = models.OneToOneField(Nivel,null=True,on_delete=models.CASCADE)