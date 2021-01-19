from django import forms


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


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
