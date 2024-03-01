# email_app/urls.py
from django.urls import path
from .views import send_email, success_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = ([
    path('', send_email, name='send_email'),
    path('success/', success_view, name='success'),
]
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
