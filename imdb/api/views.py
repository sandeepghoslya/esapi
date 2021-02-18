from .models import MoviesDetails
from .serializers import MoviesDetailsSerializer
from rest_framework import viewsets


class MoviesDetailsModelViewSet(viewsets.ModelViewSet):
    queryset = MoviesDetails.objects.all()
    serializer_class = MoviesDetailsSerializer

