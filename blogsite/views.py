from django.shortcuts import render
from blog.models import Post
from portfolio.models import Project

def index (request):
    posts = Post.objects.order_by('-pub_date')[:5]
    projects = Project.objects.order_by('-pub_date')[:5]
    context = {'posts': posts, 'projects': projects}
    return render(request, 'site/index.html', context)