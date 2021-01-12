from django import forms

from recipe_user.models import Author

# from django.forms import ModelForm




# class SignupForm(ModelForm):

#     class Meta:
#         model = Author
#         fields = ('username', 'email')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    bio = forms.CharField(max_length=140, required=False)
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    emailform = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    messageform = forms.CharField(widget=forms.Textarea, required=True)





