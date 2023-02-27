from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractBaseUser):
    email = models.CharField(max_length=120),
    password = models.CharField(max_length=120)

