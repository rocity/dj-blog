from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('email', 'content', 'url')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }
