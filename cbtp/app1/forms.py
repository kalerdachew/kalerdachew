from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from app1.models import kal,Mother,mother_vaccine,child
class registerform1(forms.ModelForm):
 
 class Meta:
   model = Mother
   fields = '__all__'
class registerform2(forms.ModelForm):
    class Meta:
     model = mother_vaccine 
     fields = '__all__'
    
class registerform3(forms.ModelForm):
    
    class Meta:
        model = child
        fields = '__all__'


  
  
 