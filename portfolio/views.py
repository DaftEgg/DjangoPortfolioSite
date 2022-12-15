from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})