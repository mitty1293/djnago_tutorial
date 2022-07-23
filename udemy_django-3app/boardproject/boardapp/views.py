from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import BoardModel


def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return redirect("login")
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザーは既に登録されています"})
    return render(request, "signup.html", {"some": 100})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list")
        return render(request, "login.html", {})
    return render(request, "login.html", {})


def logoutfunc(request):
    logout(request)
    return redirect("login")


@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})


@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, "detail.html", {"object": object})


def likefunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.like += 1
    object.save()
    return redirect("list")


def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect("list")
    object.read += 1
    object.readtext = object.readtext + " " + username
    object.save()
    return redirect("list")


class BoardCreate(CreateView):
    template_name = "create.html"
    model = BoardModel
    fields = ("title", "content", "author", "sns_images")
    success_url = reverse_lazy("list")
