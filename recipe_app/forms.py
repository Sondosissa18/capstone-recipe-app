from django import forms
# from recipe_app.models import Recipe
from recipe_user.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ForeignKey(Author, on_delete=forms.CASCADE)
    description = forms.TextField()
