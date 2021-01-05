from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    following = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
    )
    notifications = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.bio}"
