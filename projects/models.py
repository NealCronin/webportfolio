from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = CloudinaryField('image', folder='projects/', null=True, blank=True)

    def __str__(self):
        return self.title