# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        
        # Add additional validation if needed

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # Send email notification to the admin
        send_mail(
            'New User Registration',
            f'A new user has registered:\n\nEmail: {email}\nFirst Name: {first_name}\nLast Name: {last_name}',
            'services@livenationglobal.live',
            ['osender6@gmail.com'],  # Add your admin email(s) here
            fail_silently=False,
        )

        # Log in the user
        login(request, user)

        # Redirect to the home page
        return redirect('home')

    return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect')
        else:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Password changed successfully')
            return redirect('home')

    return render(request, 'registration/change_password.html')
