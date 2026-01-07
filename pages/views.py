import re
from django.shortcuts import render, get_object_or_404
from projects.models import Project
from pages.models import GalleryImage, GalleryVideo

def home_view(request):
    projects = Project.objects.filter(is_visible=True).order_by('order')
    for project in projects:
        try:
            img = GalleryImage.objects.get(slug=project.image_slug)
            project.thumbnail_url = img.image.url
        except (GalleryImage.DoesNotExist, AttributeError):
            project.thumbnail_url = ""
    return render(request, 'pages/home.html', {'projects': projects})

def about_view(request):
    return render(request, 'pages/about.html')

def resume_view(request):
    return render(request, 'pages/resume.html')

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    # Start with the raw body text
    content = project.body if project.body else ""

    # 1. FIX VIDEOS: Find every [[video:slug]] and replace it
    # We find all matches first
    video_matches = re.findall(r'\[\[video:(.*?)\]\]', content)
    
    for video_slug in video_matches:
        try:
            # Look up the video object
            v_obj = GalleryVideo.objects.get(slug=video_slug.strip())
            v_url = v_obj.video_file.url
            # Replace the shortcode with the actual URL string
            content = content.replace(f"[[video:{video_slug}]]", v_url)
        except GalleryVideo.DoesNotExist:
            # If slug is wrong, replace with a dummy link so it doesn't 404
            content = content.replace(f"[[video:{video_slug}]]", "#video-not-found")

    # 2. FIX IMAGES: Do the same for images
    image_matches = re.findall(r'\[\[image:(.*?)\]\]', content)
    for img_slug in image_matches:
        try:
            i_obj = GalleryImage.objects.get(slug=img_slug.strip())
            content = content.replace(f"[[image:{img_slug}]]", i_obj.image.url)
        except GalleryImage.DoesNotExist:
            content = content.replace(f"[[image:{img_slug}]]", "")

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'processed_body': content,  # Use this new variable in your template!
    })