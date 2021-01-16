from django import forms
from recipe_app.models import Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        exclude = ('author', 'saved')
        widgets = {
            "items": forms.Textarea(),
            "instructions": forms.Textarea(),
            "description": forms.Textarea(),
        }


class AddMessageForm(forms.Form):
    text = forms.CharField(max_length=140)


