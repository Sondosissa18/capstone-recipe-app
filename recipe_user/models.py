from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    name = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200)
    following = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
    )
    notifications = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} "


class Message(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='messages')

    def __str__(self):
        return f"{self.text} - {self.author}"
