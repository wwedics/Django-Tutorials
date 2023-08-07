from django.db import models

# Create your models here.
class Contact(models.Model):
    location = models.CharField(max_length=402)
    email = models.CharField(max_length=402)
    phone = models.CharField(max_length=402)
    name = models.CharField(max_length=402)

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
