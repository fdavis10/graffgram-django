from django import forms
from .models import  Post, Comment

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

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder':'Комментарий здесь!',
            'rows': 4,
            'cols':50
        }
    ))
    
    class Meta:
        model = Comment
        fields = ['content']

