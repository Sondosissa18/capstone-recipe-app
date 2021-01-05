from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import Author, Recipe
# class CustomUserAdmin(UserAdmin):
#     model = Author

# admin.site.register(Author, CustomUserAdmin)


from recipe_app.models import Recipe


admin.site.register(Recipe)


