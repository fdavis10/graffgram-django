from django import forms
from .models import  Post, Comment

class AddPostForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=Post.STATUS_OF_WORK,
        widget=forms.Select,
        required=True,
        label="Статус работы"
    )
    class Meta:
        model = Post
        fields = ['image', 'description', 'status']
#         widgets = {
#         'status': forms.Select(choices=Post.STATUS_OF_WORK),
# }

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

