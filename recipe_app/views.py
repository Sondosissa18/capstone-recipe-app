from recipe_app.models import Author
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from recipe_app.models import Author, Recipe
from django.views.generic import TemplateView, View

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from .forms import LoginForm, RegisterForm

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
