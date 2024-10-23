# store/tests.py
from django.test import TestCase
from django.urls import reverse

class StoreViewTests(TestCase):
    
 def test_categories_page(self):
        response = self.client.get(reverse('categories/'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Categories")
def test_fashion_trends_page(self):
        response = self.client.get(reverse('trends'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fashion Trends")

def test_profile_page(self):
       response = self.client.get(reverse('profile'))
       self.assertEqual(response.status_code, 200)
       self.assertContains(response, "My Profile")
def test_about_page(self):
         response = self.client.get(reverse('about'))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "About Us")

def test_social_page(self):
         response = self.client.get(reverse('social'))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "Social Media")
