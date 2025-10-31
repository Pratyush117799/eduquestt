from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')
<<<<<<< HEAD
=======

>>>>>>> 9beaa37 (add quiz removed)


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

def signup_teacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup_teacher.html')

        # ✅ Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Try another one.")
            return render(request, 'signup_teacher.html')

        # ✅ If not exists, create new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        messages.success(request, "Teacher account created successfully.")
        return redirect('login_teacher')

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
<<<<<<< HEAD
    
@login_required(login_url='login_teacher')
def dashboard_teacher(request):
    return render(request, 'dashboard_teacher.html')


def leaderboard(request):
    return render(request, 'leaderboard.html')

def lecture(request):
    return render(request, 'lecture.html')
=======

<<<<<<< HEAD
def leaderboard(request):
    return render(request, 'leaderboard.html')
>>>>>>> af3dd2e ( leader board added)
=======

def dashboard_teacher(request):
    teacher_profile, created = TeacherProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                student = User.objects.get(username=username)
                if student in teacher_profile.students.all():
                    messages.warning(request, f"Student '{username}' is already added.")
                else:
                    teacher_profile.students.add(student)
                    messages.success(request, f"✅ Student '{username}' added successfully!")
            except User.DoesNotExist:
                messages.error(request, "❌ No student found with that username.")
            return redirect('dashboard_teacher')
    else:
        form = AddStudentForm()

    students = teacher_profile.students.all()
    return render(request, 'dashboard_teacher.html', {'form': form, 'students': students})



>>>>>>> 9beaa37 (add quiz removed)
