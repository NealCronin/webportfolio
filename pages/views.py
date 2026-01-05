from django.shortcuts import render
from projects.models import Project  # Import the Project model from your other app

def home_view(request):
    """
    Renders the landing page. 
    """
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'pages/home.html', context)

def about_view(request):
    """
    Renders the about page.
    """
    return render(request, 'pages/about.html')