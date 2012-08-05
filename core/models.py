from django.db import models
from amadeus import settings

# Create your models here.

urlDefaultProfileImage = settings.STATIC_ROOT,'/assets/img/profile.png'

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=20, unique=True)
    #role = models.ForeignKey(Role)
    #cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=8)
    sex = models.CharField(max_length=1)
    birthday = models.DateField(blank=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    formacaoPrincipal = models.CharField(max_length=100)
    anoFormacaoPrincipal = models.CharField(max_length=4)
    cursoFormacaoPrincipal = models.CharField(max_length=100)
    instituicaoFormacaoPrincipal = models.CharField(max_length=100)
    dadosCurriculares = models.CharField(max_length=300)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    profileImage = models.FileField(upload_to='user/profileImages', default='user/profile.png', blank=True, null=True)
    

    def __unicode__(self):
        return self.name
