from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import Field
from django.forms import widgets
from django.urls import reverse
from datetime import date


class Agenda(models.Model):
    name = models.CharField(max_length=255)
    data = models.DateField()
    hour = models.TimeField()
    information = models.CharField(max_length=255, default=None)
    


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['hour','data',]
    

class Data(models.Model):
    data = models.DateField( max_length=25 ,default='asdoasd')