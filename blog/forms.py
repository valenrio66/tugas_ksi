from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=False)
    body = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'email']
