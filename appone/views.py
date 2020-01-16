from django.shortcuts import render
from .models import VideoStreamingLinks
from .serializers import VideoSerializer

from rest_framework.viewsets import ModelViewSet

class VideoPlay(ModelViewSet):
    queryset = VideoStreamingLinks.objects.all()
    serializer_class = VideoSerializer