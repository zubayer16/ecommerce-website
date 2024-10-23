from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import store, cart


class TestUrls(SimpleTestCase):

	def test_store_url_is_resolved(self):
		url = reverse('store')
		print(resolve(url))
		self.assertEqual(resolve(url).func,store)


