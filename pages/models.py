import os
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Your Name")
    nav_bar_title = models.CharField(max_length=100, default="Your Name")
    home_page_title = models.CharField(max_length=200, default="Blurb")

    about_bio_full = models.TextField(default="This is your about me bio. Edit it in the admin panel.")
    about_email = models.EmailField(default="Your@email.com")
    about_linkedin = models.URLField(blank=True)

    profile_picture_slug = models.CharField(max_length=100, blank=True)
    wip_image_slug = models.CharField(max_length=100, blank=True)
    
    resume_filename = models.CharField(
        max_length=100, 
        default="default_resume",
        help_text="Enter the filename (without .pdf) located in static/docs/"
    )

    light_bg_color = models.CharField(max_length=7, default="#ffffff")
    light_text_color = models.CharField(max_length=7, default="#1f2937")
    light_nav_bar_color = models.CharField(max_length=7, default="#ffffff")
    light_accent_color = models.CharField(max_length=7, default="#e63946")

    dark_bg_color = models.CharField(max_length=7, default="#121212")
    dark_text_color = models.CharField(max_length=7, default="#f3f4f6")
    dark_nav_bar_color = models.CharField(max_length=7, default="#121212")
    dark_accent_color = models.CharField(max_length=7, default="#ff8c00")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Global Site Settings"

class GalleryImage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.name

class GalleryVideo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    video_file = CloudinaryField('video', resource_type='video')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery Video"
        verbose_name_plural = "Gallery Videos"