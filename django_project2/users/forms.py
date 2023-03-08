from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import profile
class userregister(UserCreationForm):
 email=forms.EmailField()
 class Meta:
    model=User
    fields=['username','email','password1','password2']
class updateform(forms.ModelForm):
  email=forms.EmailField()
  class Meta:
    model=User
    fields=['username','email'] 
class profileupdateform(forms.ModelForm):
  class Meta:
    model=profile
    fields=['image']
    #picture=models.forms.FileField(, max_length=, required=False)
   
