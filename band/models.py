# band/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import CustomUser

class Band(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextUploadingField()
    cover_image = models.ImageField(upload_to='band_covers/', blank=True, null=True)
    # Add more fields as needed

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Band"
        verbose_name_plural = "Bands"

class MembershipType(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='membership_types')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.name}"

    class Meta:
        verbose_name = "Membership Type"
        verbose_name_plural = "Membership Types"

class Membership(models.Model):
    PAYMENT_CHOICES = [
        ('Zelle', 'Zelle'),
        ('Paypal', 'Paypal'),
        ('Cash App', 'Cash App'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash Mailing', 'Cash Mailing'),
        ('Crypto', 'Crypto'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='memberships')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='memberships')
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    country = models.CharField(max_length=100, default="test country")
    state = models.CharField(max_length=100, default="test state")
    city = models.CharField(max_length=100, default="test city")
    address = models.TextField(default="test address")
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.band} - {self.membership_type} - {self.payment_type}"

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

        
class VacationPricing(models.Model):
    name = models.CharField(max_length=255, default="Week 1")
    price = models.DecimalField(max_digits=8, decimal_places=0, default="1000")

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Vacation Price"
        verbose_name_plural = "Vacation Prices"
        
class Vacation(models.Model):
    PAYMENT_CHOICES = [
        ('Zelle', 'Zelle'),
        ('Paypal', 'Paypal'),
        ('Cash App', 'Cash App'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash Mailing', 'Cash Mailing'),
        ('Crypto', 'Crypto'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vacations')
    name = models.CharField(max_length=255)  # Combine first and last name from CustomUser
    email = models.EmailField()  # Get email from CustomUser
    country = models.CharField(max_length=100)
    preferred_destination = models.CharField(max_length=255)
    favourite_artist_band = models.CharField(max_length=255)
    benefit_card_copy = models.ImageField(upload_to='benefit_card_copies/', blank=True, null=True)
    preferred_dates = models.DateField()
    phone_number = models.CharField(max_length=20)  # Include country code
    address = models.TextField()
    special_requests = models.TextField()
    select_week = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(max_length=20)
    preferred_payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    price = models.ForeignKey(VacationPricing, on_delete=models.CASCADE, related_name='vacation_price')

    def __str__(self):
        return f"{self.user.email} - {self.name} Vacation"

    class Meta:
        verbose_name = "Vacation"
        verbose_name_plural = "Vacations"


class Autograph(models.Model):
    PAYMENT_CHOICES = [
        ('Zelle', 'Zelle'),
        ('Paypal', 'Paypal'),
        ('Cash App', 'Cash App'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash Mailing', 'Cash Mailing'),
        ('Crypto', 'Crypto'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='autographs')
    name = models.CharField(max_length=255)  # Combine first and last name from CustomUser
    email = models.EmailField()  # Get email from CustomUser
    country = models.CharField(max_length=100)
    band = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)  # Include country code
    address = models.TextField()
    preferred_dates = models.DateField()
    preferred_payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.name} Autograph"

    class Meta:
        verbose_name = "Autograph"
        verbose_name_plural = "Autographs"


class GeneralMembership(models.Model):
    PAYMENT_CHOICES = [
        ('Zelle', 'Zelle'),
        ('Paypal', 'Paypal'),
        ('Cash App', 'Cash App'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash Mailing', 'Cash Mailing'),
        ('Crypto', 'Crypto'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='general_memberships')
    band = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    country = models.CharField(max_length=100, default="test country")
    state = models.CharField(max_length=100, default="test state")
    city = models.CharField(max_length=100, default="test city")
    address = models.TextField(default="test address")
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.band} - {self.membership_type.name} - {self.payment_type.name}"

    class Meta:
        verbose_name = "General Membership"
        verbose_name_plural = "General Memberships"
