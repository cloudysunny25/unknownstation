from django import forms
from .models import Post,Category
from django.contrib.auth.models import User
from django.forms import ModelForm,PasswordInput
#from markdownx.fields import MarkdownxFormField



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
