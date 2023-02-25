from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    first_name.widget.attrs.update({'class': 'form-control form-control-lg'})
    username.widget.attrs.update({'class': 'form-control form-control-lg'})
    email.widget.attrs.update({'class': 'form-control form-control-lg'})
    password1.widget.attrs.update({'class': 'form-control form-control-lg'})
    password2.widget.attrs.update({'class': 'form-control form-control-lg'})

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }


class LogInForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    username.widget.attrs.update({'class': 'form-control form-control-lg '})
    password.widget.attrs.update({'class': 'form-control form-control-lg'})

    class Meta:
        fields = [
            'email',
            'password',
        ]
