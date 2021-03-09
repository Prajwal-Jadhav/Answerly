import django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account was successfully created.')
            return redirect(reverse('main:home'))
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {"form": form})
