from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("Email should be provided"))

        email = self.normalize_email(email)
        new_user = self.models(email=email, **kwargs)
        new_user.set_password(password)
        new_user.save()
        
        return new_user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        if kwargs.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))
        
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))
        
        if kwargs.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))
        
        return self.create_user(email, password, **kwargs)
    
    
class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=True, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']
    objects = CustomUserManager()
    
    def __str__(self):
        return f"<User {self.email}>"

            
