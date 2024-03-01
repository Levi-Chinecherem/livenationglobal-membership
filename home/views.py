# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # Create a new contact record
        Contact.objects.create(name=name, email=email, message=message_content)

        # Send email notification to the admin
        send_mail(
            'New Contact Form Submission',
            f'A new message has been received from the contact form:\n\nName: {name}\nEmail: {email}\nMessage: {message_content}',
            'services@livenationglobal.live',
            ['osender6@gmail.com'],  # Add your admin email(s) here
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

