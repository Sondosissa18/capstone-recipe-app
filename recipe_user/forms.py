from django import forms


class RecipeUserForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.TextField()
    username = forms.CharField(max_length=150)