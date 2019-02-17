from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author_id = models.TextField()
    author_name = models.TextField()
    main_text = models.TextField()
    image_path = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    