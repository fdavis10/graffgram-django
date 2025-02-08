from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm, CommentForm

def popular_post(request):
    posts = Post.objects.prefetch_related('comments').all()
    for post in posts:
        post.last_comment = post.comments.order_by('-created').first()

    return render(request, 'blog/posts/post_page.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    comments = post.comments.all()
    return render(request, 'blog/posts/post_detail.html', {'post': post, 'comments': comments})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:popular_posts')
    return redirect('blog:popular_posts')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = request.user in post.likes.all()
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return JsonResponse({'likes_count': post.likes.count(), 'liked': not liked})
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user
            post.save()
            return redirect('blog:popular_posts')
    else:
        form = AddPostForm()

    return render(request, 'blog/posts/create_post.html', {'form': form})
