from django.db import models
from django.utils import timezone
from django.urls import reverse
class Reporter(models.Model):
    full_name=models.CharField( max_length=100)
    def __str__(self):
        return self.full_name
class Article(models.Model):
    Title=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    reporter=models.ForeignKey(Reporter, on_delete=models.CASCADE,related_name="reporter_serial")   #to delete articles if the user manually delete them
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("magazine_detail", kwargs={"pk": self.pk})
    
    