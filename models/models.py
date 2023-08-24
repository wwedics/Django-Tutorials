from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
    


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    title = models.CharField(max_length=402)

    def __str__(self):
        return self.album



  
class Book(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)

    def __str__(self):
        return self.title

