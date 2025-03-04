from rest_framework import serializers
from .models import News
from django.core.exceptions import ValidationError


class NewsSerializer(serializers.ModelSerializer):
    image_video = serializers.ImageField(required=False)

    class Meta:
        model = News
        fields = ['uid','title', 'body', 'image_video']



class NewsCreateSerializer(serializers.ModelSerializer):
    image_video = serializers.FileField(required=True)

    class Meta:
        model = News
        fields = ['uid', 'title', 'body', 'type', 'image_video']

    def validate(self, data):
        """Ensure file type matches the selected type (image or video)."""
        file = data.get("image_video")
        news_type = data.get("type")

        if not file:
            raise ValidationError({"image_video": "You must upload either an image or a video."})

        valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
        valid_video_types = ['video/mp4', 'video/avi', 'video/mov', 'video/mkv']

        file_type = file.content_type  # Get uploaded file type

        if news_type == "image" and file_type not in valid_image_types:
            raise ValidationError({"image_video": "Uploaded file must be an image."})
        elif news_type == "video" and file_type not in valid_video_types:
            raise ValidationError({"image_video": "Uploaded file must be a video."})

        return data
