from django import forms

from recipe_user.models import Author


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter your Username....',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter your Password....',
        }
    ))


class SignupForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter your email....',
        }
    ))
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter your username....',
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter your password....',
        }
    ))
    # bio = forms.CharField(max_length=140, required=False, widget=forms.Textarea(
    #     attrs = {
    #         'class':'form-control',
    #         'placeholder':'Enter your bio....',
    #     }
    # ))

class ContactForm(forms.Form):
    emailform = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    messageform = forms.CharField(widget=forms.Textarea, required=True)





