from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, telephone, nom, prenom, email, npi, code_postal, password=None, **extra_fields):
        if not telephone:
            raise ValueError("L'utilisateur doit avoir un numéro de téléphone")
        user = self.model(
            telephone=telephone,
            nom=nom,
            prenom=prenom,
            email=self.normalize_email(email),
            npi=npi,
            code_postal=code_postal,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, email, password, telephone=None, nom='Admin', prenom='User', npi='0000', code_postal='0000', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')
        user = self.create_user(
            telephone=telephone if telephone else '0000000000',
            nom=nom,
            prenom=prenom,
            email=email,
            npi=npi,
            code_postal=code_postal,
            password=password,
            **extra_fields
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=60)
    email=models.CharField(max_length=25, unique=True)
    telephone=models.CharField(max_length=15)
    npi=models.CharField(max_length=15)
    code_postal=models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    def has_module_perms(self, app_label):
       return self.is_superuser or self.groups.filter(permissions__codename='can_view_' + app_label).exists()

    def has_perm(self, perm, obj=None):
       return self.is_superuser or self.groups.filter(permissions__codename=perm).exists()

class UserProfile(models.Model):
    email= models.EmailField(unique=True,max_length=25)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.telephone} {self.motdepasse}"


class Projects(models.Model):
    nom=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    