from django.db import models
from recipe_app.models import Recipe
from django.utils import timezone
from recipe_user.models import Author, Message


class Notifications(models.Model):
    text = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(Author, related_name='recipe_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)
