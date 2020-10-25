from django.db import models
from datetime import date


class User(models.Model):
    panchayath = models.CharField(max_length=30)
    ward= models.CharField(max_length=30,null=True)
    name  = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30)
    
class Category(models.Model):
      category = models.CharField(max_length=30)

class Scheme(models.Model):
    schemename = models.CharField(max_length=30)
    datepub =  models.DateField(default=date.today)
    validdate =  models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


