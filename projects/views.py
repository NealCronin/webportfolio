from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """Shows all projects"""
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    """Shows a single project's documentation"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})