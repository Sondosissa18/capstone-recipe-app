from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from recipe_app.models import Recipe
from recipe_user.models import Author

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.forms import LoginForm, SignupForm
import random

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic.list import ListView

from .forms import AddRecipeForm, AddMessageForm
from django.conf import settings
from django.utils.decorators import method_decorator
from datetime import datetime


class RecipeDetailView(View):
    def get(self, request, recipe_id):
        my_recipe = Recipe.objects.get(id=recipe_id)
        return render(request, "recipe_detail.html",
                      {"recipes": my_recipe})


@login_required(login_url="/login")
def index_view(request):
    now = datetime.now().time()
    four_am = now.replace(hour=4, minute=0, second=0, microsecond=0)
    ten_am = now.replace(hour=10, minute=0, second=0, microsecond=0)
    four_pm = now.replace(hour=16, minute=0, second=0, microsecond=0)
    ten_pm = now.replace(hour=22, minute=0, second=0, microsecond=0)
    # recipes = Recipe.objects.all()
    if now > four_am and now < ten_am:
        breakfast_recipes = Recipe.objects.all().filter(category='BREAKFAST')
        ids = []
        for n in breakfast_recipes:
            ids.append(n.id)
        random_ids = random.sample(ids, 3)
    elif now > ten_am and now < four_pm:
        lunch_recipes = Recipe.objects.all().filter(category='LUNCH')
        ids = []
        for n in lunch_recipes:
            ids.append(n.id)
        random_ids = random.sample(ids, 3)
    elif now > four_pm and now < ten_pm:
        dinner_recipes = Recipe.objects.all().filter(category='DINNER')
        ids = []
        for n in dinner_recipes:
            ids.append(n.id)
        random_ids = random.sample(ids, 3)
    elif now > ten_pm and now < four_am:
        snack_recipes = Recipe.objects.all().filter(category='SNACKS')
        ids = []
        for n in snack_recipes:
            ids.append(n.id)
        random_ids = random.sample(ids, 3)
    one_recipe = Recipe.objects.get(id=random_ids[0])
    two_recipe = Recipe.objects.get(id=random_ids[1])
    three_recipe = Recipe.objects.get(id=random_ids[2])
    return render(
        request, "home.html", {
                "one_recipe": one_recipe,
                "two_recipe": two_recipe,
                "three_recipe": three_recipe,
                # "form": form,
                # "signup_form": signup_form
            })


def saved_recipe_view(request):
    user = request.user
    user_id = request.user.id
    recipes = user.saved.all()
    personal_recipes = Recipe.objects.filter(author=user_id)
    return render(request, 'saved_recipes.html', {'recipes': recipes, 
                                                  'personal_recipes': personal_recipes})


def helper(request, recipe_id, save):
    user = request.user
    recipe = Recipe.objects.filter(id=recipe_id).first()
    if save:
        recipe.saved.add(user)
        recipe.save()
    else:
        recipe.saved.remove(user)
        recipe.save()


def save_view(request, recipe_id):
    save = True
    helper(request, recipe_id, save)
    return HttpResponseRedirect(reverse('homepage'))


def unsave_view(request, recipe_id):
    save = False
    helper(request, recipe_id, save)
    return HttpResponseRedirect(reverse('homepage'))


def about_view(request):
    return render(request, "about.html")


class SearchBar(LoginRequiredMixin, View):
    def get(self, request):
        html = "search.html"
        search = request.GET.get('search')
        post = Recipe.objects.all().filter(title=search)
        return render(request, html, {'post': post})




# help from Matt with this request.FILES upload.
@login_required(login_url="/login")
# @login_required
def recipe_upload(request):
    if request.method == "POST":
        # my_p = Author.objects.get(user=request.user.username)
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            recipe_instance = Recipe.objects.create(
                title=data['title'],
                author=request.user,
                description=data['description'],
                items=data['items'],
                timerequired=data['timerequired'],
                instructions=data['instructions'],
                image=data['image']
            )
            return redirect(reverse("recipe_detail_view", args=[recipe_instance.id]))
    form = AddRecipeForm()
    return render(request, 'recipe_upload.html', {'form': form})


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html',  status=500)



@login_required()
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    html = 'generic_view.html'
    # breakpoint()
    if request.user.username is recipe.author.username or request.user.is_staff:
        if request.method == "POST":
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                recipe.title = form.data['title']
                recipe.description = form.data['description']
                recipe.items = form.data['items']
                recipe.timerequired = form.data['timerequired']
                recipe.instructions = form.data['instructions']
                recipe.save()
                return HttpResponseRedirect(reverse('recipe_detail_view', kwargs={'recipe_id': recipe_id}))
        data = {
            'title': recipe.title,
            'author': recipe.author,
            'description': recipe.description,
            'timerequired': recipe.timerequired,
            'items': recipe.items,
            'instructions': recipe.instructions,
            }
        form = AddRecipeForm(initial=data)
        return render(request, html, {'form': form})
    else:
        return render(request, 'not_auth.html')

#    title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     description = models.TextField()
#     items = models.TextField(max_length=140, default='ingredients')
#     timerequired = models.CharField(max_length=100)
#     instructions = models.TextField()
#     image = models.ImageField(upload_to="media/", null=True, blank=True)
#     saved = models.ManyToManyField(Author, related_name='saved')
#     MEAL_CHOICES = (
#         ("BREAKFAST", "Breakfast"),
#         ("LUNCH", "Lunch"),
#         ("DINNER", "Dinner"),
#         ("SNACKS", "snacks"),
#         ("DESSERT", "Dessert"),
#         ("OTHER", "Other"),
#         )
#     category = models.CharField(max_length=10, choices=MEAL_CHOICES)