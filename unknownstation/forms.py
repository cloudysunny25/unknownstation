from django import forms
from .models import Post,Category
from django.contrib.auth.models import User
from django.forms import ModelForm,PasswordInput,TextInput
from django.contrib.auth.forms import AuthenticationForm
#from markdownx.fields import MarkdownxFormField



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

    '''def validation(self,user):
        if user is None:
            raise forms.ValidationError(
                _("The username is not exist."),
                code='username',
            )
        if user.  '''
