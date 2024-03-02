# band/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Band, Autograph, Vacation, MembershipType, Membership
from django.contrib import messages
from django.core.mail import send_mail
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def membership_success(request):
    return render(request, 'band/membership_success.html')

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'band/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, 'band/band_detail.html', {'band': band})


@login_required
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


@login_required
def create_vacation(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        preferred_destination = request.POST.get('preferred_destination')
        favourite_artist_band = request.POST.get('favourite_artist_band')
        benefit_card_copy = request.FILES.get('benefit_card_copy')
        preferred_dates = request.POST.get('preferred_dates')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        special_requests = request.POST.get('special_requests')
        select_week = request.POST.get('select_week')
        emergency_contact_phone = request.POST.get('emergency_contact_phone')
        preferred_payment_method = request.POST.get('preferred_payment_method')

        # Assuming you have a function to get the payment choices
        payment_choices = Vacation.PAYMENT_CHOICES()

        if not preferred_dates:
            messages.error(request, 'Please select preferred dates.')
            return redirect('create_vacation')

        # Convert preferred_dates to a DateField format
        preferred_dates = date.fromisoformat(preferred_dates)

        # Get user details from the request
        user = request.user
        name = f"{user.first_name} {user.last_name}"
        email = user.email

        # Create the Vacation object
        Vacation.objects.create(
            user=user,
            name=name,
            email=email,
            country=country,
            preferred_destination=preferred_destination,
            favourite_artist_band=favourite_artist_band,
            benefit_card_copy=benefit_card_copy,
            preferred_dates=preferred_dates,
            phone_number=phone_number,
            address=address,
            special_requests=special_requests,
            select_week=select_week,
            emergency_contact_phone=emergency_contact_phone,
            preferred_payment_method=preferred_payment_method
        )

        messages.success(request, 'Vacation created successfully.')
        return redirect('vacation_success')

    # Assuming you have a function to get the payment choices
    payment_choices = Vacation.PAYMENT_CHOICES

    context = {
        'payment_choices': payment_choices,
    }

    return render(request, 'band/vacation.html', context)

@login_required
def vacation_success(request):
    return render(request, 'band/vacation_success.html')

@login_required
def create_autograph(request):

    if request.method == 'POST':
        country = request.POST['country']
        band_name = request.POST['band']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        preferred_dates = request.POST['preferred_dates']
        preferred_payment_method = request.POST['preferred_payment_method']

        user = request.user
        email = user.email
        full_name = f"{user.first_name} {user.last_name}"

        Autograph.objects.create(
            user=user,
            name=full_name,
            email=email,
            country=country,
            band=band_name,
            phone_number=phone_number,
            address=address,
            preferred_dates=preferred_dates,
            preferred_payment_method=preferred_payment_method
        )

        messages.success(request, 'Autograph request submitted successfully!')
        return redirect('home')

    payment_choices = Autograph.PAYMENT_CHOICES  # Make sure to define PAYMENT_CHOICES in your Autograph model

    return render(request, 'band/autograph.html', {'payment_choices': payment_choices})

@login_required
def autograph_success(request):
    return render(request, 'band/autograph_success.html')



@login_required
def general_membership(request):

    payment_choices = Membership.PAYMENT_CHOICES
    if request.method == 'POST':
        user = request.user
        payment_type = request.POST.get('payment_type')
        band = request.POST.get('band')
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
            'New General Membership Registration',
            f'A new membership has been registered:\n\nUser: {user.email}\nBand: {band.name}\nMembership Type: {membership_type.name}\nMembership Price: ${membership_type.price}',
            'services@livenationglobal.live',
            ['osender6@gmail.com'],  # Add your admin email(s) here
            fail_silently=False,
        )

        messages.success(request, 'Membership registered successfully!')
        return redirect('membership_success')

    membership_types = MembershipType.objects.all()
    return render(request, 'band/band_membership.html', {'membership_types': membership_types, 'payment_choices': payment_choices})
