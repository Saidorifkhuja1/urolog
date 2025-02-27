from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    image_video = serializers.ImageField(required=False)

    class Meta:
        model = News
        fields = ['uid','title', 'body', 'image_video']
