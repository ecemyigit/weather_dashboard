from django.test import TestCase
from django.contrib.auth.models import User
from .models import Favorite
from django.urls import reverse

class WeatherAppTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_index_view(self):
        # Test the index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Weather Dashboard')

    def test_add_favorite(self):
        # Test adding a favorite city
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/add_favorite/', {'city': 'New York'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.filter(user=self.user, city='New York').count(), 1)

    def test_remove_favorite(self):
        # Test removing a favorite city
        Favorite.objects.create(user=self.user, city='Los Angeles')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/remove_favorite/', {'city': 'Los Angeles'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.filter(user=self.user, city='Los Angeles').count(), 0)
