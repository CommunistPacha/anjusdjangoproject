from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
def login_view(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user=None
        if user and user.Check_password(password):
            login(request,user)
            return redirect('home')
        else:
            error="invalid email or password"
    return render(request,'login.html',{'error':error})

# Create your views here.
