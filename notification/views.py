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
    notes = Notifications.objects.filter(user=request.user, viewed=False)
    save_render = render(
        request,
        "message.html",
        {
            "notes": notes,
        }
    )
    for notification in notes:
        notification.viewed = True
        notification.save()
    return save_render


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