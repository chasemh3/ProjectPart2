from django.db import models

# Create your models here.

class Customer(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)  
    race = models.CharField(max_length=10)  



