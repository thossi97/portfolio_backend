from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to="media", default="default.jpg")
    #git = models.URLField()
    url = models.URLField(blank=True)
    description = models.TextField()
