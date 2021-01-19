from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from recipe_user.models import Author
from recipe_app.models import Recipe
from django.contrib.auth.views import LogoutView
from authentication.forms import LoginForm, SignupForm, ContactForm
from django.views.generic import View
from django.contrib import messages

from django.core.mail import send_mail

# @login_required()
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        signup_form = SignupForm(request.POST)
        if Author.objects.filter(username=form.data["username"]).first() == None:
            if signup_form.is_valid():
                
                data = signup_form.cleaned_data
                Author.objects.create_user(
                        username=data["username"], 
                        email=data["email"],
                        password=data["password"]
                    )
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("login"))
                    )
        if form.is_valid():
            data = form.cleaned_data
            # if Author.objects.filter(username=data["username"]).first() == []:
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {user.username}")
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = LoginForm()
    signup_form = SignupForm()
    return render(request, "login.html", {"form": form, "signup_form": signup_form})

# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request, username=data["username"], password=data["password"]
#             )
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {user.username}")
#                 return redirect("homepage")
                
#             else:
#                 messages.error(request, "Invalid username or password")
#         else:
#             messages.error(request, "Invalid username or password")
#     form = LoginForm()
#     return render(request, "login.html", {"form": form})

# class Signup_view(View):
#     def get(self, request):
#         signup_form = SignupForm()
#         return render(request, "signup.html", {"signup_form": signup_form})

#     def post(self, request):
#         signup_form = request.POST
#         form = SignupForm(signup_form)
#         if form.is_valid():
#             data = form.cleaned_data
#             Author.objects.create_user(
#                 username=data["username"], 
#                 email=data["email"],
#                 password=data["password"]
#             )
#             return HttpResponseRedirect(
#                     request.GET.get("next", reverse("homepage"))
#                 )

# /////testing 

# class Signup_view(View):
#     def get(self, request):
#         signup_form = SignupForm()
#         return render(request, "signup.html", {"signup_form": signup_form}) 

#     def post(self, request):
#         signup_form = request.POST
#         form = SignupForm(signup_form)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = Author.objects.create_user(
#                 username=data["username"], 
#                 email=data["email"],
#                 password=data["password"]
#             )
#            login(request, user)
#             return HttpResponseRedirect(reverse("homepage"))

class Signup_view(View):
    def get(self, request):
        signup_form = SignupForm()
        return render(request, "signup.html", {"signup_form": signup_form}) 

    def post(self, request):
        signup_form = request.POST
        form = SignupForm(signup_form)
        if form.is_valid():
            data = form.cleaned_data
            user = Author.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"]
            )
            if user:
                login(request, user)
                messages.info(request, "Succefully Created, Welcome to Stuff Yo Face!!!")
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
            else:
                messages.error(request, "Unfortunately, there was a problem , Try again..")
        else:
            messages.error(request, "Unfortunately, there was a problem , Try again..")
            return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login/")


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "Contactpage.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            emailform = form.cleaned_data['emailform']
            subject = form.cleaned_data['subject']
            messageform = form.cleaned_data['messageform']
            send_mail(subject, messageform, emailform,['sondosissa18@gmail.com', emailform ])
            return render(request, "Contactpage.html", {"form": form})


# /////convert it to class base view
# def contactview(request):
    # if request.method == "GET":
    #     form = ContactForm()
    # else:
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         emailform = form.cleaned_data['emailform']
    #         subject = form.cleaned_data['subject']
    #         messageform = form.cleaned_data['messageform']
    #         send_mail(subject, messageform, emailform,['sondosissa18@gmail.com', emailform ])

    # return render(request, "Contactpage.html", {"form": form})