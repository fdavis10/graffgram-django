from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def popular_post(request):
    popular_posts = Post.objects.prefetch_related('comments').all()
    for post in popular_posts:
        post.last_comment = post.comments.order_by('-created').first()

    return render(request, 'blog/posts/post_page.html', {'popular_posts': popular_posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    comments = post.comments.all()
    return render(request, 'blog/posts/post_detail.html', {'post': post, 'comments': comments})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))