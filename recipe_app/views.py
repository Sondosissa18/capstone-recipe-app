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
from datetime import datetime


# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request, username=data["username"], password=data["password"]
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(
#                     request.GET.get("next", reverse("home"))
#                 )
#     form = LoginForm()
#     return render(request, "login.html", {"form": form})

# @login_required()
# def recipe_detail_view(request, recipe_id):
#     my_recipe = Recipe.objects.get(id=recipe_id)
#     return render(request, "recipe_detail.html", {"recipes": my_recipe})


class RecipeDetailView(View):
    def get(self, request, recipe_id):
        my_recipe = Recipe.objects.get(id=recipe_id)
        return render(request, "recipe_detail.html",
                      {"recipes": my_recipe})


# def following_view(request, user_id):
#     if request.user.id == user_id:
#         # you cant follow yourself
#         return HttpResponseRedirect(reverse("home"))
#     follows = Author.objects.get(id=user_id)

#     allfollowers = request.user.following.all()

#     if follows not in allfollowers:
#         request.user.following.add(follows)
#     else:
#         request.user.following.remove(follows)
#     return HttpResponseRedirect(reverse("home"))

#4-10 breakfast
# 10-4 16hours lunch
#4-10 dinner 16-22
#10-4 snacks 22-4
# form = LoginForm()
# signup_form = SignupForm()
# def breakfast(request):
#     breakfast_recipes = Recipe.objects.all().filter(category='BREAKFAST')
#     ids = []
#     for n in breakfast_recipes:
#         ids.append(n.id)
#     random_ids = random.sample(ids, 3)
#     one_recipe = Recipe.objects.get(id=random_ids[0])
#     two_recipe = Recipe.objects.get(id=random_ids[1])
#     three_recipe = Recipe.objects.get(id=random_ids[2])
#     return one_recipe, two_recipe, three_recipe


# def lunch(request):
#     lunch_recipes = Recipe.objects.all().filter(category='LUNCH')
#     ids = []
#     for n in lunch_recipes:
#         ids.append(n.id)
#     random_ids = random.sample(ids, 3)
#     print(random_ids)
#     one_recipe = Recipe.objects.get(id=random_ids[0])
#     two_recipe = Recipe.objects.get(id=random_ids[1])
#     three_recipe = Recipe.objects.get(id=random_ids[2])
#     print(one_recipe)
#     return render(
#         request, "home.html", {
#                 "one_recipe": one_recipe,
#                 "two_recipe": two_recipe,
#                 "three_recipe": three_recipe,
#                 # "form": form,
#                 # "signup_form": signup_form
#             })


# def dinner(request):
#     dinner_recipes = Recipe.objects.all().filter(category='DINNER')
#     ids = []
#     for n in dinner_recipes:
#         ids.append(n.id)
#     random_ids = random.sample(ids, 3)
#     one_recipe = Recipe.objects.get(id=random_ids[0])
#     two_recipe = Recipe.objects.get(id=random_ids[1])
#     three_recipe = Recipe.objects.get(id=random_ids[2])
#     return one_recipe, two_recipe, three_recipe


# def snacks(request):
#     snack_recipes = Recipe.objects.all().filter(category='SNACKS')
#     ids = []
#     for n in snack_recipes:
#         ids.append(n.id)
#     random_ids = random.sample(ids, 3)
#     one_recipe = Recipe.objects.get(id=random_ids[0])
#     two_recipe = Recipe.objects.get(id=random_ids[1])
#     three_recipe = Recipe.objects.get(id=random_ids[2])
#     return one_recipe, two_recipe, three_recipe


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


# class IndexView(View):
#     def get(self, request):
#         return render(request, "home.html", 
#                       {"recipes": Recipe.objects.all(),
#                        "message": Message.objects.all()})


# @login_required
# def recipe_detail_view(request):
#     html = "generic_form.html"
#     if request.method == "POST":
#         form = AddRecipeForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_recipe = Recipe.objects.create(
#                 title=data['title'],
#                 description=data['description'],
#                 author=data['author']
#             )
#             return HttpResponseRedirect(reverse("homepage"))
        
#     form = AddRecipeForm()
#     return render(request, html, {'form': form})


# ///////seeems not correct 
# @login_required
# def message_view(request):
#     html = "generic_form.html"
#     if request.method == "POST":
#         form = AddMessageForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Message.objects.create(
#                 text=data['text'],
#                 created_at=data['created_at'],
#                 author=data['author']
#             )
#             return HttpResponseRedirect(reverse("homepage"))

#     form = AddMessageForm()
#     return render(request, html, {'form': form})


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
            return redirect(reverse("recipe_detail_view", args=[recipe_instance.id]))
    form = AddRecipeForm()
    return render(request, 'recipe_upload.html', {'form': form})
