from django.db import models
from django.contrib.auth.models import User      #importing users of the site
from PIL import Image     #importing image module form pillow package
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) #making a one to one connection with the USER model
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} profile'
    def save(self):
        super().save()
        img=Image.open(self.image.path)      #opening the path of the current user image
        if img.height >300 and img.width>300:
            output_size=(100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

# Create your models here.
