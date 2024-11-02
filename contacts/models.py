from datetime import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,default=datetime.now)
    
    responded_view = models.BooleanField(blank=True,default=False)


    def __str__(self):
        return self.email


class NonCarContact(models.Model):
    full_name = models.CharField(max_length=100)
    
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    
    created_date = models.DateTimeField(blank=True,default=datetime.now)
    
    responded_view = models.BooleanField(blank=True,default=False)


    def __str__(self):
        return self.email