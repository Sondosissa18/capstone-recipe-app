from django.db import models
from recipe_user.models import Author


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    items = models.TextField(max_length=140, default='ingredients')
    timerequired = models.CharField(max_length=100)
    instructions = models.TextField()
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    saved = models.ManyToManyField(Author, null=True, related_name='saved')

    def __str__(self):
        return f"{self.title} - {self.author}"
