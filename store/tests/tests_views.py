from django.test import TestCase,Client
from django.urls import reverse
from store.models import Customer, Product, Order
import json


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.store_url = reverse('store')
		self.cart_url = reverse('cart')
		self.checkout_url = reverse('checkout')

	def test_store_GET(self):

		response = self.client.get(self.store_url)

		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'store/store.html')


	def test_cart_GET(self):

		response = self.client.get(self.cart_url)

		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'store/cart.html')

	def test_checkout_GET(self):

		response = self.client.get(self.checkout_url)

		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'store/checkout.html')



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




