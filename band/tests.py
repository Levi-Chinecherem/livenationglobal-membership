# band/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Band, MembershipType

class BandViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )

        # Create a test band and membership type
        self.band = Band.objects.create(name='Test Band', description='Test description')
        self.membership_type = MembershipType.objects.create(
            band=self.band,
            name='Test Membership',
            price=100.00,
            duration='One Year'
        )

    def test_band_list_view(self):
        # Test the band list view
        response = self.client.get(reverse('band_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band/band_list.html')

    def test_band_detail_view(self):
        # Test the band detail view
        response = self.client.get(reverse('band_detail', args=[self.band.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band/band_detail.html')

    def test_join_band_view(self):
        # Test the join band view
        self.client.force_login(self.user)
        response = self.client.get(reverse('join_band', args=[self.band.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band/join_band.html')

        # Test form submission
        response = self.client.post(reverse('join_band', args=[self.band.id]), {
            'preferred_payment_type': 'Credit Card',
            'membership_type': self.membership_type.id,
            # Add other fields as needed
        })
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after successful form submission

        # Add more assertions as needed

    def test_common_fields_detail_view(self):
        # Test the common fields detail view
        self.client.force_login(self.user)
        response = self.client.get(reverse('common_fields_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band/common_fields_detail.html')

        # Test form submission
        response = self.client.post(reverse('common_fields_detail'), {
            'full_name': 'John Doe',
            'address': '123 Main St',
            'phone_number': '123-456-7890',
            'country': 'USA',
            'state': 'California',
            'city': 'San Francisco',
        })
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after successful form submission

        # Add more assertions as needed

    def test_membership_type_list_view(self):
        # Test the membership type list view
        self.client.force_login(self.user)
        response = self.client.get(reverse('membership_type_list', args=[self.band.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band/membership_type_list.html')

    def test_membership_type_detail_view(self):
        # Test the membership type detail view
        response = self.client.get(reverse('membership_type_detail', args=[self.membership_type.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band/membership_type_detail.html')
