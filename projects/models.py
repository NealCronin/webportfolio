from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    flavor_text = models.TextField()
    order = models.CharField(max_length=200)
    image = CloudinaryField('image', default='https://res.cloudinary.com/dmo5atv6g/image/upload/v1767583908/WIP.png', folder="/pr")
    body = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title