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

from django.contrib.auth.views import LogoutView
# from recipe_user import views as user_views
from authentication import views as auth_views
from recipe_app import views as recipe_views
from notification import views as notifica_views


from recipeapp import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns = [
    path('', recipe_views.IndexView.as_view(), name="homepage"),
    path('recipes/<int:recipe_id>/', recipe_views.RecipeDetailView.as_view(),
         name="recipe_detail_view"),
    path('message/', notifica_views.message_view, name="message_view"),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('signup/', auth_views.signup_view, name="signup"),
    # path('results/', recipe_views.SearchView.as_view(), name='search'),
    path('searchbar/', recipe_views.search_bar, name='searchbar'),
    path('recipe-upload/', recipe_views.recipe_upload, name='upload')



]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
