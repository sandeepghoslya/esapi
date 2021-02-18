from django.contrib import admin
from .models import MoviesDetails


@admin.register(MoviesDetails)
class MoviesDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'released_year', 'rating', 'genres']
