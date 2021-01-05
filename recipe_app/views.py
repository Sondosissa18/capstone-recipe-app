from recipe_app.models import Author
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from recipe_app.models import Recipe
from recipe_user.models import Message
# from django.views.generic import TemplateView, View

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from .forms import AddRecipeForm, AddMessageForm

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

@login_required()
def recipe_detail_view(request, recipe_id):
    my_recipes = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": my_recipes})


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


def index_view(request):
    return render(
        request, "home.html", {
                "recipes": Recipe.objects.all(),
                "message": Message.objects.all()
            })


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


@login_required
def message_view(request):
    html = "generic_form.html"
    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                text=data['text'],
                created_at=data['created_at'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddMessageForm()
    return render(request, html, {'form': form})
