# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    #id field is added automatically by django
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + " " + str(customer_id)
