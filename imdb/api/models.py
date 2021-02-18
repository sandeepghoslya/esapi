from django.db import models


class MoviesDetails(models.Model):
    title = models.CharField(max_length=50)
    released_year = models.IntegerField()
    rating = models.FloatField(blank=True, null=True)
    genres = models.CharField(max_length=100)


