from django.contrib import admin
from .import models
from django.contrib.auth.models import User
# # from django.contrib.auth.admin import UserAdmin
admin.site.register(models.Mother)
admin.site.register(models.child)
admin.site.register(models.mother_vaccine)
admin.site.register(models.child_vaccine)
admin.site.register(models.kal)
admin.site.register(models.disease)
#unregistering the user from the admin dashboard
# @admin.register(User)
# class NewAdmin(UserAdmin): 
#     readonly_fields = [ 
#         'date_joined', 
#     ] 
# # Register your models here.
# from django.contrib.auth.admin import UserAdmin 
# admin.site.unregister(User)
# @admin.register(User,UserAdmin) 
# class UserAdmin(UserAdmin): 
#     readonly_fields = [ 
#         'date_joined', 
#     ] 