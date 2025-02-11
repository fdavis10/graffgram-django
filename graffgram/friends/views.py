from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FriendShip
from django.contrib.auth.models import User

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    friendship, created = FriendShip.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect('user_profile', user_id=user_id)

@login_required
def accept_to_friend(request, friendship_id):
    friendship = get_object_or_404(FriendShip, id=friendship_id, to_user=request.user)
    friendship.status = 'accepted'
    friendship.save()
    return redirect('friend_requests')

@login_required
def decline_to_friend(request, friendship_id):
    friendship = get_object_or_404(FriendShip, id=friendship_id, to_user = request.user)
    friendship.status = 'declined'
    friendship.save()
    return redirect('friends_requests')

@login_required
def view_friendship_requests(request):
    requests_friendship = FriendShip.objects.filter(to_user=request.user, status='pending')
    return render(request, 'friendship_requests.html', {'requests_friendship': requests_friendship})


@login_required
def view_friends(request):
    friends = FriendShip.objects.filter(from_user = request.user, status='accepted')|FriendShip.objects.filter(to_user=request.user, status='accepted')
    return render(request, 'friends_list.html', {'friends':friends})