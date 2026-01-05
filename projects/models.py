from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=100)

    image = CloudinaryField('image', default='https://res.cloudinary.com/dmo5atv6g/image/upload/v1767583908/WIP.png', folder="/projects/")

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title