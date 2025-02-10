from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from .models import User
from blog.models import Post

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
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'upload-input'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'input textarea', 'placeholder':'Расскажи о себе'}), required=False)
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input email'}), required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'image',
            'phone_number',
            'bio'
        )