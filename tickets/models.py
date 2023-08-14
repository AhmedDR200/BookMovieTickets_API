from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    hall = models.CharField(max_length=30)
    date = models.DateField(auto_now=False, auto_now_add=True)



class Guest(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)



class Reservation(models.Model):
    movie = models.ForeignKey(Movie,related_name='reservation', on_delete=models.CASCADE)  # Foreign Key to the model 'movie'
    guest= models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
