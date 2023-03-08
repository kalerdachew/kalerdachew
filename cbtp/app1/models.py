from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
     
class Mother(models.Model):
    blood_types=(
        ("1","A"),
        ("2","B"),
        ("3","O"),
        ("4","A+"),
        ("5","B+"),
        ("6","O+"),
        ("7","A-"),
        ("7","B-"),
        ("7","O-"),
    )
    countrycodes=(
('220',   'Gambia'),
('221',   'Senegal'),
('222',   'Mauritania'),
('223',  'Mali'),
('251'   ,'Ethiopia'),
("265",   "Malawi"),
("266"   ,"Lesotho"),
("267","Botswana"),
("268",  "Eswatini"),
("269","Comoros"),
("27","South Africa"),
    )
    firstname=models.CharField(max_length=10)
    middlename=models.CharField( max_length=10)
    lastname=models.CharField( max_length=10)
    birthday=models.DateTimeField(default=timezone.now)
    bloodtype=models.CharField(max_length=10,choices=blood_types,default=3)
   # mobilephone=PhoneNumberField(choices=countrycodes,default=251)
    zone=models.CharField(max_length=20)
    woreda=models.CharField(max_length=20)
    kebele=models.CharField(max_length=20)
    vaccine_id=models.IntegerField(default=0)
    mother_id=models.IntegerField(default=5)
    def __str__(self) ->str():
        return self.firstname
    

    #vaccine_model
class mother_vaccine(models.Model):
 vaccines=(
    ("1","TT1"),
    ("2","TT2"),
    ("3","TT3"),
    ("4","TT4"),
    ("5","TT5"),
    ("6","RH")
)
 vaccine_name=models.CharField(max_length=10,choices=vaccines)
 vaccine_date=models.DateField(default=timezone.now)
 def __str__(self):
       return self.vaccine_name
class child(models.Model):
    blood_types=(
        ("1","A"),
        ("2","B"),
        ("3","O"),
        ("4","A+"),
        ("5","B+"),
        ("6","O+"), 
        ("7","A-"),
        ("7","B-"),
        ("7","O-"),
    )
    #mothername=models.OneToOneField(Mother.firstname, on_delete=models.CASCADE)
   # mothername=models.OneToOneField(Mother, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50,primary_key=True)
    middlename=models.TextField(max_length=50)
    lastname=models.CharField(max_length=50)
    birthday=models.DateTimeField(default=timezone.now)
    bloodtype=models.CharField(max_length=10,choices=blood_types,default=3)
    def __str__(self):
         return self.firstname
class child_vaccine(models.Model):
    vaccines=(
        ("1","R1"),
        ("2","R2"),
        ("3","R3"),
        ("4","R4"),
        ("5","R5"),
    )
    
    vaccine_name=models.CharField(max_length=10,choices=vaccines)
    child_name=models.OneToOneField(child, on_delete=models.CASCADE)
    def __str__(self):
         return self.vaccine_name
     

class kal(models.Model):    
    username=models.CharField(max_length=20)
    password=models.TextField(max_length=25)
    Age=models.IntegerField(default=20)
    def __str__(self):
       return self.username
    
class vaccine_permissions(models.Model):
    product_name=models.CharField(max_length=50)
    product_id=models.IntegerField(default=0)
    product_price=models.FloatField(default=0.0)
    class Meta:
        permissions=[('can_change_vaccine_catagory','change catagory')]
class disease(models.Model):
    name=models.CharField(max_length=10)
    rate=models.FloatField(default=0.0)
    def __str__(self):
        return self.name
    
   
