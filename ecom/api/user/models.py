from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50,default='Anoynmous')
    email = models.EmailField(max_length=200,unique=True)#ensure no email repeat
    username=None
    USERNAME_FIELD='email' #whiever unique identifier
    REQUIRED_FIELDS = []
    phone=models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    session_token = models.CharField(max_length=10, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)