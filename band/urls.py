# band/urls.py
from django.urls import path
from .views import general_membership, band_list, band_detail, create_membership, create_autograph, autograph_success, membership_success, create_vacation, vacation_success

urlpatterns = [
    path('', band_list, name='band_list'),
    path('<int:band_id>/', band_detail, name='band_detail'),
    path('<int:band_id>/create_membership/', create_membership, name='create_membership'),
    path('general/membership/', general_membership, name='general_membership'),
    path('success/', membership_success, name='membership_success'),
    path('create_vacation/', create_vacation, name='create_vacation'),
    path('vacation_success/', vacation_success, name='vacation_success'),
    path('create_autograph/', create_autograph, name='create_autograph'),
    path('autograph_success/', autograph_success, name='autograph_success'),
]
