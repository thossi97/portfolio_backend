from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=False, upload_to="project_pics")
    git = models.URLField(blank=True)
    url = models.URLField(blank=True)
    description = models.TextField()

