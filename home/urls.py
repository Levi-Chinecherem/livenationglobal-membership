# band/urls.py
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)