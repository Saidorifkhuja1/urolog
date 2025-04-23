from rest_framework import serializers
from .models import News
from django.core.exceptions import ValidationError


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['uid', 'title', 'body', 'photo1', 'photo2', 'photo3', 'photo4', 'video', 'uploaded_at']


class NewsCreateSerializer(serializers.ModelSerializer):
    photo1 = serializers.ImageField(required=True)
    photo2 = serializers.ImageField(required=False)
    photo3 = serializers.ImageField(required=False)
    photo4 = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)

    class Meta:
        model = News
        fields = ['uid', 'title', 'body', 'photo1', 'photo2', 'photo3', 'photo4', 'video']

    def validate(self, data):
        """Validate photo and video file types"""
        # Validate required photo1
        photo1 = data.get("photo1")
        if not photo1:
            raise ValidationError({"photo1": "You must upload at least one photo."})

        valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
        valid_video_types = ['video/mp4', 'video/webm', 'video/ogg', 'video/avi', 'video/mov', 'video/mkv']

        # Check photo1 content type
        if photo1.content_type not in valid_image_types:
            raise ValidationError({"photo1": "Uploaded file must be an image."})

        # Check optional photos if provided
        for field_name in ['photo2', 'photo3', 'photo4']:
            photo = data.get(field_name)
            if photo and photo.content_type not in valid_image_types:
                raise ValidationError({field_name: "Uploaded file must be an image."})

        # Check video if provided
        video = data.get("video")
        if video and video.content_type not in valid_video_types:
            raise ValidationError({"video": "Uploaded file must be a video in MP4, WebM, OGG, AVI, MOV, or MKV format."})

        return data




# from rest_framework import serializers
# from .models import News
# from django.core.exceptions import ValidationError
#
#
# class NewsSerializer(serializers.ModelSerializer):
#     image_video = serializers.ImageField(required=False)
#
#     class Meta:
#         model = News
#         fields = ['uid','title', 'body', 'type', 'image_video']
#
#
#
# class NewsCreateSerializer(serializers.ModelSerializer):
#     image_video = serializers.FileField(required=True)
#
#     class Meta:
#         model = News
#         fields = ['uid', 'title', 'body', 'type', 'image_video']
#
#     def validate(self, data):
#         """Ensure file type matches the selected type (image or video)."""
#         file = data.get("image_video")
#         news_type = data.get("type")
#
#         if not file:
#             raise ValidationError({"image_video": "You must upload either an image or a video."})
#
#         valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
#         valid_video_types = ['video/mp4', 'video/avi', 'video/mov', 'video/mkv']
#
#         file_type = file.content_type  # Get uploaded file type
#
#         if news_type == "image" and file_type not in valid_image_types:
#             raise ValidationError({"image_video": "Uploaded file must be an image."})
#         elif news_type == "video" and file_type not in valid_video_types:
#             raise ValidationError({"image_video": "Uploaded file must be a video."})
#
#         return data
