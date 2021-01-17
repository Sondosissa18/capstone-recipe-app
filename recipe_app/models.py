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
    saved = models.ManyToManyField(Author, related_name='saved')
    MEAL_CHOICES = (
        ("BREAKFAST", "Breakfast"),
        ("LUNCH", "Lunch"),
        ("DINNER", "Dinner"),
        ("SNACKS", "snacks"),
        ("DESSERT", "Dessert"),
        ("OTHER", "Other"),
        )
    category = models.CharField(max_length=10, choices=MEAL_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.author}"
