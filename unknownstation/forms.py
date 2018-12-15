from django import forms
from .models import Post,User,Category
from django.forms import ModelForm,PasswordInput
from markdownx.fields import MarkdownxFormField


class PostForm(forms.Form):

    content = MarkdownxFormField()

'''
class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('nickname', 'password',)
'''
