from django.db import models
from django.contrib.auth.models import AbstractUser

class BUser(AbstractUser):
    head = models.CharField(max_length=200,default='', verbose_name="头像地址")

