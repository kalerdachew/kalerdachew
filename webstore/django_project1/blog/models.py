from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class post(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    post_content=models.TextField(max_length=100)
    def __str__(self):
        return self.title

   #post_set method
   # post_set.create
   # post_set.all()      user1=post_set.all()--> to see posts written by user1