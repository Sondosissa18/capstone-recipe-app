"""recipeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from django.contrib.auth.views import LogoutView


# from recipe_user import views as user_views


# from authentication import views as auth_views

from recipe_app import views as recipe_views

# from notification import views as notifica_views


urlpatterns = [
    path('', recipe_views.index_view, name="homepage"),
    path('recipes/', recipe_views.recipe_detail_view, name="recipe_detail_view"),
    path('message/', recipe_views.message_view, name="message_view"),
    path('admin/', admin.site.urls)
]
