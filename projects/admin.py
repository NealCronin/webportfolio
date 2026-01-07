from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.urls import reverse
from django.utils.html import format_html
from .models import Project
from pages.models import GalleryImage, GalleryVideo

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_slug', 'order', 'is_visible')
    list_editable = ('order', 'is_visible')
    
    readonly_fields = ('gallery_link', 'video_gallery_link')
    
    fields = (
        'is_visible', 
        'title',
        'image_slug',
        'flavor_text',
        'order', 
        'gallery_link', 
        'video_gallery_link',  
        'body'
    )

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 40,
                'cols': 120,
            })
        },
    }

    def gallery_link(self, obj):
        url = reverse('admin:pages_galleryimage_changelist')
        return format_html(
            '<a href="{}" target="_blank" style="font-weight:bold;">'
            '🖼️ Open Image Gallery to find Slugs</a>', 
            url
        )
    gallery_link.short_description = "Image Library"

    def video_gallery_link(self, obj):
        url = reverse('admin:pages_galleryvideo_changelist')
        return format_html(
            '<a href="{}" target="_blank" style="font-weight:bold;">'
            '🎬 Open Video Gallery to find Slugs</a>', 
            url
        )
    video_gallery_link.short_description = "Video Library"

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['image_slug'].help_text = "Lookup slug in Image Gallery."
        return super().render_change_form(request, context, *args, **kwargs)