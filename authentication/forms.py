from django import forms

from recipe_user.models import Author


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(Author, required=False)
    password = forms.CharField(widget=forms.PasswordInput)