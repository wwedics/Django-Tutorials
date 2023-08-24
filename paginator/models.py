from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=402)
    username = models.CharField(max_length=402)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Users'