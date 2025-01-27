from django.shortcuts import render, get_object_or_404
from .models import Post

def popular_post(request):
    popular_posts = Post.objects.all()
    return render(request, 'blog/posts/post_page.html', {'popular_posts': popular_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    
    return render(request, 'blog/posts/post_detail.html', {'post': post})


