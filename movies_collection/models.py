from django.db import models
import uuid

# Create your models here.



class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=500)


    class Meta:
        '''
        to set table name in database
        '''
        db_table = "genre"

    
class Movie(models.Model):
    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "movie"



class Collection(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title =  models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500)
    movies = models.ManyToManyField(Movie)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "collection"

