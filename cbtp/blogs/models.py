from django.db import models

# Create your models here.
class blogs(models.Model):
    Title=models.CharField(max_length=15,primary_key=True)
    content=models.TextField(max_length=100)
    author=models.CharField(max_length=50)
    date_published=models.DateField()
    def __str__(self):
     return self.Title
 
     