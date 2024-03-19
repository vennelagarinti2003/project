from django.db import models

# Create your models here.

class hospitalregistermodel(models.Model):   
    name=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=12) 
    address=models.CharField(max_length=100)
    workinghrs=models.CharField(max_length=10) 
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class hospitalloginmodel(models.Model):   
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class hospitalhomemodel(models.Model):  
    name=models.CharField(max_length=35)
    contact_no=models.CharField(max_length=12) 
    specialy=models.CharField(max_length=30)
    address=models.CharField(max_length=100)  
    image=models.ImageField()
    
class bloodbank(models.Model):
    name=models.CharField(max_length=20) 
    phone_no=models.CharField(max_length=12)
    address=models.CharField(max_length=100) 
    bloodavali=models.IntegerField()
