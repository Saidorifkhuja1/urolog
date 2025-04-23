import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class News(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()

    # Multiple photo fields
    photo1 = models.ImageField(upload_to='news/photos/')
    photo2 = models.ImageField(upload_to='news/photos/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='news/photos/', null=True, blank=True)
    photo4 = models.ImageField(upload_to='news/photos/', null=True, blank=True)

    # Video field
    video = models.FileField(upload_to='news/videos/', null=True, blank=True)

    uploaded_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        """Ensure file types are valid."""
        valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
        valid_video_types = ['video/mp4', 'video/webm', 'video/ogg']

        # Check photo1 (required)
        if not self.photo1:
            raise ValidationError({"photo1": "You must upload at least one photo."})

        if hasattr(self.photo1.file, 'content_type') and self.photo1.file.content_type not in valid_image_types:
            raise ValidationError({"photo1": "Uploaded file must be an image."})

        # Check optional photos if provided
        for field_name in ['photo2', 'photo3', 'photo4']:
            field = getattr(self, field_name)
            if field and hasattr(field.file, 'content_type') and field.file.content_type not in valid_image_types:
                raise ValidationError({field_name: "Uploaded file must be an image."})

        # Check video if provided
        if self.video and hasattr(self.video.file,
                                  'content_type') and self.video.file.content_type not in valid_video_types:
            raise ValidationError({"video": "Uploaded file must be a video in MP4, WebM, or OGG format."})

    def save(self, *args, **kwargs):
        """Run validation before saving."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def get_photos(self):
        """Return a list of all photos that are not None."""
        photos = []
        for i in range(1, 5):
            photo = getattr(self, f'photo{i}')
            if photo:
                photos.append(photo)
        return photos



















# import uuid
# from django.db import models
# from django.utils import timezone
# from django.core.exceptions import ValidationError
#
#
# class News(models.Model):
#     TYPE_CHOICES = [
#         ('image', 'Image'),
#         ('video', 'Video'),
#     ]
#     uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
#     title = models.CharField(max_length=250)
#     body = models.TextField()
#     type = models.CharField(max_length=100, choices=TYPE_CHOICES)
#     image_video = models.FileField(upload_to='news/', null=True, blank=True)
#     uploaded_at = models.DateTimeField(default=timezone.now)
#
#     def clean(self):
#         """Ensure file type matches the selected type (image or video)."""
#         if not self.image_video:
#             raise ValidationError({"image_video": "You must upload either an image or a video."})
#
#         valid_image_types = ['image/jpeg', 'image/png', 'image/gif']
#         valid_video_types = ['video/mp4', 'video/webm', 'video/ogg']
#
#         file_type = self.image_video.file.content_type
#
#         if self.type == "image" and file_type not in valid_image_types:
#             raise ValidationError({"image_video": "Uploaded file must be an image."})
#         elif self.type == "video" and file_type not in valid_video_types:
#             raise ValidationError({"image_video": "Uploaded file must be a video."})
#
#     def save(self, *args, **kwargs):
#         """Run validation before saving."""
#         self.clean()
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title