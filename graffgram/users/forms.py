from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Номер телефона'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'password1',
            'password2'
        )

        username = forms.CharField()
        email = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
        )

        email = forms.CharField()
