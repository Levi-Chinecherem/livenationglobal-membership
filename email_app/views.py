# email_app/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings
from django.template.loader import render_to_string

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_info = form.save()
            send_custom_email(email_info)
            return redirect('success')  # You need to define a success URL in urls.py
    else:
        form = EmailForm()

    return render(request, 'email/index.html', {'form': form})

def send_custom_email(email_info):
    subject = f"Message from {email_info.company_name} - {email_info.purpose}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email_info.to_email]

    # Load your custom email template
    email_template = 'email/email1.html'
    
    # Render the template with user-provided data
    email_content = render_to_string(email_template, {
        'company_name': email_info.company_name,
        'purpose': email_info.purpose,
        'message_content': email_info.message_content,
    })

    send_mail(subject, '', from_email, recipient_list, html_message=email_content)

def success_view(request):
    return render(request, 'email/success.html')
