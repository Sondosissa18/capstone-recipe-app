from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from recipe_app.models import Recipe
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
    recipes = Recipe.objects.all()
    db_recipes = recipes.count()
    randomlist = random.sample(range(1, db_recipes), 3)
    one_recipe = Recipe.objects.get(id=randomlist[0])
    two_recipe = Recipe.objects.get(id=randomlist[1])
    three_recipe = Recipe.objects.get(id=randomlist[2])
    return render(
        request, "home.html", {
                "one_recipe": one_recipe,
                "two_recipe": two_recipe,
                "three_recipe": three_recipe,
            })


def saved_recipe_view(request):
    user = request.user
    recipes = user.saved.all()
    return render(request, 'saved_recipes.html', {'recipes': recipes})


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


def error_404_view(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500_view(request):
    data = {}
    return render(request, '500.html', data)


# help from Matt with this request.FILES upload. 
def recipe_upload(request):
    if request.method == "POST":
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
            breakpoint()
            return redirect(reverse("recipe_detail_view", args=[recipe_instance.id]))
    form = AddRecipeForm()
    return render(request, 'recipe_upload.html', {'form': form})


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html',  status=500)
