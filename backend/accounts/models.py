from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class User(AbstractBaseUser):
    COUNTRY_CHOICES = (
        ('Bangladesh', 'Bangladesh'),
        ('India', 'India'),
    )
    username                = models.CharField(max_length=155, unique=True)
    email                   = models.EmailField(max_length=254, unique=True)
    phone_number            = models.CharField(_("phone number"), max_length=15, unique=True)
    country                 = models.CharField(_("country"), max_length=15, choices=COUNTRY_CHOICES)
    address                 = models.CharField(max_length=1000)
    avatar                  = models.ImageField(upload_to=f'avatar/{id}/', default='user/avatar.png')
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    joined_date             = models.DateTimeField(verbose_name='date join', auto_now_add=True)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_admin                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        #Simplest possible answer: Yes, always
        return True

