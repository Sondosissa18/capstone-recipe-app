from recipe_app.models import Author
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from recipe_app.models import Recipe
from recipe_user.models import Message
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


# @login_required()
# def recipe_detail_view(request, recipe_id):
#     my_recipe = Recipe.objects.get(id=recipe_id)
#     return render(request, "recipe_detail.html", {"recipes": my_recipe})


class RecipeDetailView(View):
    def get(self, request, recipe_id):
        my_recipe = Recipe.objects.get(id=recipe_id)
        return render(request, "recipe_detail.html",
                      {"recipes": my_recipe})


# @login_required(login_url="/login")
def index_view(request):
    form = LoginForm()
    signup_form = SignupForm()
    recipes = Recipe.objects.all()
    how_many = recipes.count()
    one = random.randint(1, how_many)
    two = random.randint(1, how_many)
    three = random.randint(1, how_many)
    one_recipe = Recipe.objects.get(id=one)
    two_recipe = Recipe.objects.get(id=two)
    three_recipe = Recipe.objects.get(id=three)
    return render(
        request, "home.html", {
                "one_recipe": one_recipe,
                "two_recipe": two_recipe,
                "three_recipe": three_recipe,
                "form": form,
                "signup_form": signup_form
            })


def about_view(request):
    return render(request, "about.html")


# @login_required()
# def search_bar(request):
#     html = "search.html"
#     if request.method == "GET":
#         search = request.GET.get('search')
#         post = Recipe.objects.all().filter(title=search)
#         return render(request, html, {'post': post})


class SearchBar(LoginRequiredMixin, View):
    def get(self, request):
        html = "search.html"
        search = request.GET.get('search')
        post = Recipe.objects.all().filter(title=search)
        return render(request, html, {'post': post})


# help from Matt with this request.FILES upload
def recipe_upload(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=request.user,
                description=data['description'],
                items=data['items'],
                timerequired=data['timerequired'],
                instructions=data['instructions'],
                image=data['image']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()
    return render(request, 'recipe_upload.html', {'form': form})
