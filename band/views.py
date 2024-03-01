# band/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Band, MembershipType, Membership
from django.contrib import messages
from django.core.mail import send_mail
from accounts.models import CustomUser


def membership_success(request):
    return render(request, 'band/membership_success.html')

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'band/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, 'band/band_detail.html', {'band': band})

def create_membership(request, band_id):
    band = get_object_or_404(Band, id=band_id)

    payment_choices = Membership.PAYMENT_CHOICES
    if request.method == 'POST':
        user = request.user
        payment_type = request.POST.get('payment_type')
        duration = request.POST.get('duration')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        membership_type_id = request.POST.get('membership_type')

        membership_type = get_object_or_404(MembershipType, id=membership_type_id)

        # Create a new membership record
        Membership.objects.create(
            user=user,
            band=band,
            payment_type=payment_type,
            country=country,
            state=state,
            city=city,
            address=address,
            membership_type=membership_type
        )

        # Send email notification to the admin
        send_mail(
            'New Membership Registration',
            f'A new membership has been registered:\n\nUser: {user.email}\nBand: {band.name}\nMembership Type: {membership_type.name}\nMembership Price: ${membership_type.price}',
            'services@livenationglobal.live',
            ['osender6@gmail.com'],  # Add your admin email(s) here
            fail_silently=False,
        )

        messages.success(request, 'Membership registered successfully!')
        return redirect('membership_success')

    membership_types = MembershipType.objects.filter(band=band)
    return render(request, 'band/create_membership.html', {'band': band, 'membership_types': membership_types, 'payment_choices': payment_choices})
