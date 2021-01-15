from django.contrib import admin

# Register your models here.

from recipe_user.models import Author, Message


admin.site.register(Author)
admin.site.register(Message)
