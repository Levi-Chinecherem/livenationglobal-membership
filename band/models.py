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
        return f"{self.band.name} - {self.name}"

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
        return f"{self.user.email} - {self.band.name} - {self.membership_type.name} - {self.payment_type.name}"

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"
