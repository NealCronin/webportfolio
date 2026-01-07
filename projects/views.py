import re
from django.shortcuts import render, get_object_or_404
from .models import Project
from pages.models import GalleryVideo, GalleryImage

def project_list(request):
    """
    Renders the main gallery of all projects.
    """
    projects = Project.objects.filter(is_visible=True).order_by('order')
    
    # Resolve thumbnails for the list view
    for project in projects:
        try:
            if project.image_slug:
                img = GalleryImage.objects.get(slug=project.image_slug)
                project.thumbnail_url = img.image.url
            else:
                project.thumbnail_url = ""
        except (GalleryImage.DoesNotExist, AttributeError):
            project.thumbnail_url = ""
            
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    """
    Renders a single project and replaces [[video:slug]] and [[image:slug]] 
    with real Cloudinary URLs.
    """
    project = get_object_or_404(Project, slug=slug)
    content = project.body if project.body else ""

    header_image = GalleryImage.objects.filter(slug=project.image_slug).first()
    header_image_url = header_image.image.url if header_image else None

    # 1. PROCESS VIDEOS
    video_matches = re.findall(r'\[\[video:(.*?)\]\]', content)
    for v_slug in video_matches:
        original_tag = f"[[video:{v_slug}]]"
        clean_slug = v_slug.strip()
        try:
            video_obj = GalleryVideo.objects.get(slug=clean_slug)
            content = content.replace(original_tag, video_obj.video_file.url)
        except GalleryVideo.DoesNotExist:
            content = content.replace(original_tag, "#video-not-found")

    # 2. PROCESS IMAGES
    image_matches = re.findall(r'\[\[image:(.*?)\]\]', content)
    for i_slug in image_matches:
        original_tag = f"[[image:{i_slug}]]"
        clean_slug = i_slug.strip()
        try:
            image_obj = GalleryImage.objects.get(slug=clean_slug)
            content = content.replace(original_tag, image_obj.image.url)
        except GalleryImage.DoesNotExist:
            content = content.replace(original_tag, "")

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'processed_body': content, # Ensure template uses {{ processed_body|safe }}
        'header_image_url': header_image_url,
    })