from django.contrib import admin
from .import models   #importing the model from the models.py
admin.site.register(models.Article)     #registering Article class
admin.site.register(models.Reporter)    #registering Reporter class
# Register your models here.
