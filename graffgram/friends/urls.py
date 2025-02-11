from django.urls import path
from . import views

app_name = 'friemds'

urlpatterns = [
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:friendship_id>/', views.accept_to_friend, name='accept_to_friend'),
    path('decline_friend_request/<int:friendship_id>/', views.decline_to_friend, name='decline_to_friend'),
    path('friends_requests/', views.view_friendship_requests, name='friend_requests'),
    path('friends/', views.view_friends, name='friends'),
    
]
