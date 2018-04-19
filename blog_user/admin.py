from django.contrib import admin

# Register your models here.

from blog_user import models

admin.register(models.BUser)