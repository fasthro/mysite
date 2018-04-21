from django.contrib import admin

# Register your models here.
from blog import models

admin.site.register(models.TestModel)