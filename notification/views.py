from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from recipe_app.models import Author, Recipe
from django.views.generic.edit import CreateView
from notification.models import Notifications
from recipe_app.models import Recipe
from recipe_user.models import Message, Author
from notification.forms import AddMessageForm
import re


@login_required(login_url="/login")
def message_view(request):
    #  if not request.user.is_authenticated:
    #      return HttpResponseRedirect(reverse("login"))
    if request.user.is_authenticated:
        message_filter = Notifications.objects.filter(user=request.user, viewed=False)
        messages = []
        for message in message_filter:
            message = Message.objects.get(id=message.recipe_id.id)
            # Notifications.objects.filter(user=request.user, viewed=False).delete()
            messages.append(message)
        return render(request, "message.html", {"messages":messages})
    return HttpResponseRedirect(reverse("login"))


def new_message_view(request):
    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                author=request.user
            )
            text = new_message.text
            found = re.findall(r'@([A-Za-z0-9_]{1,25})', text)
            print('&&&&&&&&&', found)
            if found:
                for tag in found:
                    matched = Author.objects.get(username=tag)
                    if matched:
                        Notifications.objects.create(
                            text=new_message,
                            user=matched
                        )
        return HttpResponseRedirect(reverse('homepage'))
    form = AddMessageForm()
    html = "message_form.html"
    return render(request, html, {'form': form})

