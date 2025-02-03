from django import forms
from .models import  Post

class AddPostForm(forms.ModelForm):
    STATUS_CHOICES = Post.STATUS_OF_WORK

    status = forms.MultipleChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Статус работы'
    )

    class Meta:
        model = Post
        fields = ['image', 'description', 'status']
        widgets = {
            'decriptions': forms.Textarea(attrs={'rows': 4})
        }

