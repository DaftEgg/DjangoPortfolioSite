from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index (request):
    posts = Post.objects.order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})