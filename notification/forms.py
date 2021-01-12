from django import forms

class AddMessageForm(forms.Form):
    text = forms.CharField(max_length=140)