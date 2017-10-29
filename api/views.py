from django.shortcuts import render
from rest_framework import generics
from .serializers import GTPathSerializer
from .models import GTPath


# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = GTPath.objects.all()
    serializer_class = GTPathSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new path."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = GTPath.objects.all()
    serializer_class = GTPathSerializer
