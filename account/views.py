from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(response):
    if response.method == "post":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})


def home(request):
    return render(request, 'home.html')