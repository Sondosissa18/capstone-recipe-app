from django.forms import ModelForm
from recipe_user.models import Author


class RecipeUserForm(ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'bio')

        