from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.popular_post, name='popular_posts'),
    path('post/id/<int:pk>/', views.post_detail, name='post_detail'),
]


