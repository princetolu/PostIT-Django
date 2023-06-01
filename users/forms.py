from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form__field',
                                                             }))
    
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form__field',
                                                           }))
    
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form__field',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form__field',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form__field',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = User
        fields = ['username', 'password']
