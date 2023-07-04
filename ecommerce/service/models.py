from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    product = models.CharField(max_length=100)
