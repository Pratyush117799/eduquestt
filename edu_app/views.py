from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Passwords do not match")

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already taken")

        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()
        return redirect('login')

    # Render signup form for GET requests
    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            return HttpResponse("Invalid username or password")

    # Render login form for GET requests
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def features_page(request):
    return render(request, 'features.html')

def lecture_page(request):
    return render(request, 'lecture.html')

def signup_teacher(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Passwords do not match")

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already taken")

        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()
        return redirect('login_teacher')

    # Render signup form for GET requests
    return render(request, 'signup_teacher.html')

def login_teacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('dashboard_teacher') 
        else:
            return HttpResponse("Invalid username or password")

    # Render login form for GET requests
    return render(request, 'login_teacher.html')


@login_required(login_url='login_teacher')
def dashboard_teacher(request):
    return render(request, 'dashboard_teacher.html')