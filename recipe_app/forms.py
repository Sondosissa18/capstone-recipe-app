from django import forms

from django.utils import timezone
from recipe_user.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ForeignKey(Author, on_delete=forms.CASCADE)
    description = forms.TextField(widget=forms.Textarea)
    timerequired = forms.CharField(max_length=100)
    instructions = forms.TextField(widget=forms.Textarea)


class AddMessageForm(forms.Form):
    text = forms.CharField(max_length=140)
    created_at = forms.DateTimeField(default=timezone.now)
    author = forms.ForeignKey(Author, on_delete=forms.CASCADE, null=True, related_name='messages')
