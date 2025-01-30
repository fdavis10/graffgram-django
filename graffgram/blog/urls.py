from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.popular_post, name='popular_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/id/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]


