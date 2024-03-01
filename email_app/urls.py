# email_app/urls.py
from django.urls import path
from .views import send_email, success_view

urlpatterns = [
    path('', send_email, name='send_email'),
    path('success/', success_view, name='success'),
]
