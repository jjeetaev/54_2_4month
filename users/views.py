from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", context={"form": form})
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "users/register.html", context={"form": form})
        form.cleaned_data.__delitem__("password_confirm")
        user = User.objects.create_user(**form.cleaned_data)
        if user:
            return redirect("/")
        else:
            return render(request, "users/register.html", context={"form": form})
        
def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", context={"form": form})
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "users/login.html", context={"form": form})
        user = authenticate(**form.cleaned_data)
        if not user:
            form.add_error("pasword", "Invalid username or passwrod, try again please.")
            return render(request, "users/login.html", context={"form": form})
        login(request, user)
        return redirect("/")
    
@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect("/")
