from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class User(AbstractUser):   #abstract user provide to customize option to the default user model.
    username = None #it will avoid to take username at the time of login 
    email = models.EmailField(unique=True)
   
    
    
    objects = UserManager()
        
    USERNAME_FIELD = 'email' # it will set the email for login insteed username 
    REQUIRED_FIELDS = []