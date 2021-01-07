from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from recipe_app.models import Author, Recipe
from django.views.generic.edit import CreateView
from notification.models import Notifications
from recipe_app.models import Recipe
from recipe_user.models import Message, Author




@login_required(login_url="/login")
def message_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.user.is_authenticated:
        message_filter = Notifications.objects.filter(user=request.user, viewed=False)
        messages = []
        for message in message_filter:
            message = Message.objects.get(id=message.recipe_id.id)
            messages.append(message)
        return render(request, "message.html", {"messages":messages})
    return HttpResponseRedirect(reverse("login"))

