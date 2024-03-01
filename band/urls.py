# band/urls.py
from django.urls import path
from .views import band_list, band_detail, create_membership, membership_success

urlpatterns = [
    path('', band_list, name='band_list'),
    path('<int:band_id>/', band_detail, name='band_detail'),
    path('<int:band_id>/create_membership/', create_membership, name='create_membership'),
    path('success/', membership_success, name='membership_success'),
]
