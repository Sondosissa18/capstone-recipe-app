from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from recipe_user.models import Author
from recipe_app.models import Recipe

from django.contrib.auth.views import LogoutView
from .forms import LoginForm, SignupForm

from django.views.generic import View


# @login_required()
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "login.html", {"form": form})


class Signup_view(View):
    form_class = LoginForm

    def get(self, request):
        form = SignupForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form_class = request.POST
        form = SignupForm(form_class)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create_user(
                username=data["username"], 
                email=data["email"],
                password=data["password"]
            )
            return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
