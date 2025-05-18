from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            username = user.username  # Get username for authentication
        except User.DoesNotExist:
            user = None

        if user:
            user_auth = authenticate(
                request, username=username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('home')
            else:
                error = "Invalid email or password"
        else:
            error = "Invalid email or password"

    return render(request, 'login.html', {'error': error})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful. Please log in.")
        return redirect("login")

    return render(request, 'register.html')


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')


def search_view(request):
    return render(request, 'home.html')


def profile_view(request):
    return render(request, 'profile.html')


def about_view(request):
    return render(request, 'about.html')


def courses_view(request):
    return render(request, 'courses.html')


def teachers_view(request):
    return render(request, 'teachers.html')


def contact_view(request):
    return render(request, 'contact.html')
