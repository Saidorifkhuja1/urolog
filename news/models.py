import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class News(models.Model):
    TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    image_video = models.FileField(upload_to='news/', null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        """Ensure file type matches the selected type (image or video)."""
        if not self.image_video:
            raise ValidationError({"image_video": "You must upload either an image or a video."})

        valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
        valid_video_types = ['video/mp4', 'video/avi', 'video/mov', 'video/mkv']

        file_type = self.image_video.file.content_type  # Get uploaded file type

        if self.type == "image" and file_type not in valid_image_types:
            raise ValidationError({"image_video": "Uploaded file must be an image."})
        elif self.type == "video" and file_type not in valid_video_types:
            raise ValidationError({"image_video": "Uploaded file must be a video."})

    def save(self, *args, **kwargs):
        """Run validation before saving."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title