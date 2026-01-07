from .models import SiteSettings, GalleryImage, GalleryVideo  # Added GalleryVideo
from django.conf import settings

def site_settings(request):
    config = SiteSettings.objects.first()
    
    # 1. Helper function for Gallery Lookups
    def get_image_url(slug):
        if not slug:
            return ""
        try:
            return GalleryImage.objects.get(slug=slug).image.url
        except (GalleryImage.DoesNotExist, AttributeError):
            return ""

    # NEW: Helper function for Video Lookups
    def get_video_url(slug):
        if not slug:
            return ""
        try:
            return GalleryVideo.objects.get(slug=slug).video.url
        except (GalleryVideo.DoesNotExist, AttributeError):
            return ""

    # 2. Safety check: If no settings exist in database, return empty dict
    if not config:
        return {}

    # 3. Return the full context
    return {
        # This makes 'site_settings' available as an object in your templates
        'site_settings': config,
        
        # General Info shorthands
        'SITE_NAME': config.site_name,
        'HOME_TITLE': config.home_page_title,
        'NAV_TITLE': config.nav_bar_title,
        'ABOUT_BIO': config.about_bio_full,
        'EMAIL_ADDR': config.about_email,
        'LINKEDIN_URL': config.about_linkedin,
        
        # Asset Lookups via Slugs
        'PROFILE_PIC': get_image_url(config.profile_picture_slug),
        'WIP_IMAGE': get_image_url(config.wip_image_slug),
        'get_video_url': get_video_url,  # Passed function to lookup videos by slug

        # Design Colors (Shorthands for CSS variables)
        'L_BG': config.light_bg_color, 
        'L_TEXT': config.light_text_color,
        'L_NAV': config.light_nav_bar_color, 
        'L_ACCENT': config.light_accent_color,
        
        'D_BG': config.dark_bg_color, 
        'D_TEXT': config.dark_text_color,
        'D_NAV': config.dark_nav_bar_color, 
        'D_ACCENT': config.dark_accent_color,
    }