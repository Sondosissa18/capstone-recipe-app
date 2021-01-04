from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import Author, Recipe
# class CustomUserAdmin(UserAdmin):
#     model = Author

# admin.site.register(Author, CustomUserAdmin)


from recipe_app.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)


