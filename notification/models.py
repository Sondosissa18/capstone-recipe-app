from django.db import models
from recipe_app.models import Recipe
from django.utils import timezone
from recipe_user.models import Author


class Notifications(models.Model):
    user = models.ForeignKey(Author, related_name='recipe_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    recipe_id = models.ForeignKey(Recipe, related_name="recipe_id", on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
