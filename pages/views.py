from django.shortcuts import render, get_object_or_404
from projects.models import Project

def home_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'pages/home.html', context)

def about_view(request):
    return render(request, 'pages/about.html')

def resume_view(request):
    return render(request, 'pages/resume.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})