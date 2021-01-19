from django.contrib import admin
from django.urls import path
from authentication import views as auth_views
from recipe_app import views as recipe_views
from notification import views as notifica_views
from recipeapp import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', recipe_views.index_view, name="homepage"),
    path('recipes/<int:recipe_id>/', recipe_views.RecipeDetailView.as_view(),
         name="recipe_detail_view"),
    path('messages/', notifica_views.message_view, name="message"),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name="login"),
    path('logout/', auth_views.logout_request, name="logout"),
    path('saved-recipes/', recipe_views.saved_recipe_view, name='saved'),
    path('save/<int:recipe_id>/', recipe_views.save_view, name='save'),
    path('unsave/<int:recipe_id>/', recipe_views.unsave_view, name='unsave'),
    path('signup/', auth_views.Signup_view.as_view(), name="signup"),
    path('newmessage/', notifica_views.new_message_view, name='message'),
    path('about/', recipe_views.about_view, name="about"),
    path('contact/', auth_views.ContactView.as_view(), name='contactview'),
    path('searchbar/', recipe_views.SearchBar.as_view(), name='searchbar'),
    path('recipe-upload/', recipe_views.recipe_upload, name='upload'),
    path('editrecipe/<int:recipe_id>/', recipe_views.edit_recipe, name='edit_recipe'),
    path('breakfast/', recipe_views.breakfast_view, name='breakfast'),
    path('lunch/', recipe_views.lunch_view, name='lunch'),
    path('dinner/', recipe_views.dinner_view, name='dinner'),
    path('snacks/', recipe_views.snacks_view, name='snacks'),
    path('dessert/', recipe_views.dessert_view, name='dessert')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "recipe_app.views.error_404_view"
handler500 = "recipe_app.views.error_500_view"
