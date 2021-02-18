from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# creatig router
router = DefaultRouter()
router.register('imdbapi', views.MoviesDetailsModelViewSet, basename = 'imdb')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
