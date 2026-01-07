from django.contrib import admin
from django import forms
from .models import SiteSettings, GalleryImage, GalleryVideo
from django.utils.html import format_html

# ==========================================================================
# 1. SITE SETTINGS ADMIN
# ==========================================================================
class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'light_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_nav_bar_color': forms.TextInput(attrs={'type': 'color'}),
            'light_accent_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_nav_bar_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_accent_color': forms.TextInput(attrs={'type': 'color'}),
        }

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm
    
    fieldsets = (
        ('General Info', {
            'fields': ('site_name', 'nav_bar_title', 'home_page_title')
        }),
        ('Content & Contact', {
            'fields': ('about_bio_full', 'about_email', 'about_linkedin')
        }),
        ('Assets', {
            'fields': ('profile_picture_slug', 'wip_image_slug', 'resume_filename')
        }),
        ('Light Mode Design', {
            'fields': ('light_bg_color', 'light_text_color', 'light_nav_bar_color', 'light_accent_color')
        }),
        ('Dark Mode Design', {
            'fields': ('dark_bg_color', 'dark_text_color', 'dark_nav_bar_color', 'dark_accent_color')
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

# ==========================================================================
# 2. GALLERY IMAGES ADMIN
# ==========================================================================
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_shortcode', 'thumbnail_preview', 'uploaded_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    readonly_fields = ('get_shortcode',)

    def get_shortcode(self, obj):
        return format_html('<code>[[image:{}]]</code>', obj.slug)
    get_shortcode.short_description = "Shortcode (Copy this)"

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: auto; border-radius: 4px;" />', 
                obj.image.url
            )
        return "No Image"
    thumbnail_preview.short_description = "Preview"

@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):
    # These MUST match the fields in your new models.py exactly
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug')