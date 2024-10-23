from django.test import TestCase,Client
from django.urls import reverse
from store.models import Customer, Product, OrderItem

class TestModels(TestCase):


	def test_product(self):
		product = Product()
		product.name="A solution book"
		product.price= 200
		product.digital = True
		product.save()

		record = Product.objects.get(pk=1) 
		self.assertEqual(record,product)


	def test_orderItem(self):

		order=OrderItem()
		order.quantity = 2                             #Quantity of item
		order.product = Product()
		order.product.name="A solution book"
		order.product.price= 200                       #Price of the product
		order.product.digital = True
		order.product.save()

		order.save()


		record = OrderItem.objects.get(pk=1) 
		self.assertEqual(record.get_total,400)        #Check if expected total equal to returned total



