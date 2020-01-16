from rest_framework import serializers
from .models import VideoStreamingLinks

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoStreamingLinks
        fields = "__all__"

    