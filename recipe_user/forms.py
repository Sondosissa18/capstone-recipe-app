from django import forms
from django.forms import ModelForm


# class RecipeUserForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     bio = forms.TextField()


class RecipeUserForm(ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'bio')

        