from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.utils import timezone
from recipe_user.models import Author


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    items = models.TextField()
    timerequired = models.CharField(max_length=100)
    instructions = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
