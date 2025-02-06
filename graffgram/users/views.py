from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('main:popular_post'))
            else:
                messages.error(request, 'Неверное имя пользователя или пароль!')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.phone_number = form.cleaned_data['phone_number']
            user.save()
            auth.login(request, user)
            messages.success(
                request, f'{user.username} зарегестрировался успешно!'
            )
            return HttpResponseRedirect(reverse('blog:popular_posts'))
        else:
            messages.error(request, 'Исправьте ошибки в форме!')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {"form": form})

@login_required
def profile(request):
    user = request.user
    posts = user.post.all()
    post_count = posts.count()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен!')
            return HttpResponse(reverse('users:profile'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = ProfileForm(instance = request.user)
    
    return render(request, 'users/profile.html', {'form': form, 'user': user, 'posts': posts, 'post_count': post_count})


def logout(request):
    auth.logout(request)
    return redirect(reverse('blog:popular_posts'))        