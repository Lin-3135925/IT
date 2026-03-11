from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        # create a dummy user for login tests
        self.test_user = User.objects.create_user(
            username='testuser',
            password='Testpassword123!'
        )

    def test_signup_page_loads(self):
        """check if signup page renders properly"""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_authenticated_user_login_action(self):
        """test valid login redirects to browse page"""
        # simulate login POST
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Testpassword123!'
        })
        
        # should redirect to home/browse
        self.assertRedirects(response, reverse('browse'))
        
        # verify user is actually logged in via session
        self.assertTrue('_auth_user_id' in self.client.session)