from django import forms


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=140)
    items = forms.CharField(widget=forms.Textarea, max_length=140)
    timerequired = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea, max_length=140)
    image = forms.ImageField()


class AddMessageForm(forms.Form):
    text = forms.CharField(max_length=140)
