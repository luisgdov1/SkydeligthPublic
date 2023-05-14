from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class NewUserAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
      
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
       
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        user =  self.create_user(email, name, password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,email, name, password,**other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError('Email address is required!')
        email = BaseUserManager.normalize_email(email)
        if password is not None:
            user = self.model(email=email, name=name,password=password, **other_fields)
            user.set_password(password)
            user.save()
        else:
            user = self.model(email=email, name=name, password=password,**other_fields)
            user.set_unusable_password()
            user.save()

        return user
class NewUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(primary_key=True)
    name = models.CharField("Nombre", max_length=100,)
    sex = models.CharField("Sexo", max_length=100, null=True)
    edad = models.BigIntegerField("Edad", null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    required_password = models.BooleanField(default=False)
    
    objects = NewUserAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name",]
    
    def __str__(self):
        return f'Nombre: {self.name} Correo: {self.email}'
