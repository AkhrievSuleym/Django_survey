from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['login']
        email = request.POST['email']
        password = request.POST['psw']
        psw_check = request.POST['psw_check']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('/users/login')
    return render(request, 'users/register.html')

@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/users/profile')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/users/login")
    else:
        return render(request, 'users/login.html')

@csrf_exempt
@login_required
def profile(request):
    return render(request, 'users/profile.html')


@csrf_exempt
@login_required
def sign_out(request):
    auth_logout(request)
    return render(request, 'users/logout.html')
