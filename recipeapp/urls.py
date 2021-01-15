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
from django.conf.urls import handler404, handler500

from recipeapp import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', recipe_views.index_view, name="homepage"),
    path('recipes/<int:recipe_id>/', recipe_views.RecipeDetailView.as_view(),
         name="recipe_detail_view"),
    path('message/', notifica_views.message_view, name="message_view"),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name="login"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    path('logout/', auth_views.logout_request, name="logout"),
    path('saved-recipes/', recipe_views.saved_recipe_view, name='saved'),
    path('save/<int:recipe_id>/', recipe_views.save_view, name='save'),
    path('unsave/<int:recipe_id>/', recipe_views.unsave_view, name='unsave'),
    path('signup/', auth_views.Signup_view.as_view(), name="signup"),
    path('newmessage/', notifica_views.new_message_view, name='message'),
    path('about/', recipe_views.about_view, name="about"),
    # path('signup/', auth_views.signup_view, name="signup"),
    # path('results/', recipe_views.SearchView.as_view(), name='search'),
    path('searchbar/', recipe_views.search_bar, name='searchbar'),
    path('contact/', auth_views.ContactView.as_view(), name='contactview'),
    path('searchbar/', recipe_views.SearchBar.as_view(), name='searchbar'),
    path('recipe-upload/', recipe_views.recipe_upload, name='upload'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = recipe_views.error_404
handler500 = recipe_views.error_500
# urlpatterns += ('recipe_views.error_404_view')
# urlpatterns += ('recipe_views.error_500_view')
