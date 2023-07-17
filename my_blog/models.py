from django.db import models

# Create your models here.
class Contact(models.Model):
    location = models.CharField(max_length=402)
    email = models.CharField(max_length=402)
    phone = models.CharField(max_length=402)
    name = models.CharField(max_length=402)