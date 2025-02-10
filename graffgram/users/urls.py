from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('edit_profile/<int:pk>', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
    path('profile_user/<int:pk>', views.profile_user, name="profile_user")
]
