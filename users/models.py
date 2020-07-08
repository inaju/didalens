from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext as _
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

class AccountabilityPartner(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email = models.EmailField(_('email address'))
    phone_number=models.BigIntegerField(null=True)
    
    user=models.ForeignKey(CustomUser, null=True,verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.email)
