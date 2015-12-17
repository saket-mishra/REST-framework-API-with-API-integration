from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from datetime import datetime

class City(models.Model):
    city_name=models.CharField(max_length=100,default='',blank=False)
 
    def __str__(self):
        return self.city_name

class Person(models.Model):
    title = models.CharField(max_length=3,default="mr",blank=False)
    name = models.CharField(max_length=50,default='',blank=False)
    address = models.CharField(max_length=200,default='',blank=False)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name

class Test(models.Model):
    person = models.ForeignKey(Person)
    date = models.DateTimeField(default=datetime.now)
    test_name = models.CharField(max_length=200,default='simple blood test',blank=False)
    glucose = models.CharField(max_length=100,default='')
    hba1c = models.CharField(max_length=100,default='') 
    rbc = models.CharField(max_length=100,default='')
    wbc = models.CharField(max_length=100,default='') 
    
    def __str__(self):
        return self.test_name


