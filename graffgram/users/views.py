from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:popular_post'))
            else:
                messages.error(request, 'Неверное имя пользователя или пароль!')
        else:
            messages.error(request, 'Исправьте ошибки в форме!')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form':form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.succes(
                request, f'{user.username} зарегестрировался успешно!'
            )
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            messages.error(request, 'Исправьте ошибки в форме!')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', {"form": form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = ProfileForm(instance = request.user)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:popular_list'))        