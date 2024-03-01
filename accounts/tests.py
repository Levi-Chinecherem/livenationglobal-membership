# accounts/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AccountsViewsTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_register_view(self):
        response = self.client.post(reverse('register'), data=self.user_data)
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after successful registration
        self.assertEqual(get_user_model().objects.count(), 2)  # Assuming there's already an admin user

    def test_user_login_view(self):
        response = self.client.post(reverse('login'), data=self.user_data)
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after successful login

    def test_user_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after logout

    def test_change_password_view(self):
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        new_password_data = {
            'old_password': self.user_data['password'],
            'new_password': 'newpassword',
        }
        response = self.client.post(reverse('change_password'), data=new_password_data)
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect after successful password change
        self.assertTrue(get_user_model().objects.get(email=self.user_data['email']).check_password('newpassword'))
