from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    flavor_text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=100)
    is_visible = models.BooleanField(default=True)
    image_slug = models.CharField(
        max_length=100,
        default='work-in-progress'
    )
    # video_slug has been removed from here
    body = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order', 'title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title