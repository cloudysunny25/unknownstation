from django import forms
from .models import Post,User,Category
from django.forms import ModelForm,PasswordInput



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('nickname', 'password',)
