from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal

from .models import Product
from .services.products import ProductService


User = get_user_model()


class ProductServiceTests(TestCase):

    def setUp(self):
        self.service = ProductService()
        self.user = User.objects.create_superuser(
            username='testuser', password='testpass'
        )
        self.product = Product.objects.create(
            title='test', description='test desc',
            price='100.00', seller=self.user
        )

    def test_get_concrete(self):
        product = self.service.get_concrete(self.product.pk)
        self.assertEqual(product, self.product)

    def test_get_all(self):
        products = self.service.get_all()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], self.product)

    def test_create(self):
        new_product = self.service.create(
            title='new title', description='new desc',
            price='100.00', seller=self.user
        )
        all_products = self.service.get_all()
        self.assertEqual(len(all_products), 2)
        self.assertEqual(type(new_product), Product)
        self.assertEqual(new_product.title, 'new title')
        self.assertEqual(new_product.description, 'new desc')
        self.assertEqual(new_product.price, '100.00')
        self.assertEqual(new_product.seller, self.user)

    def test_update(self):
        product = self.service.update(
            self.product.pk, title='new title', description='new desc',
            price='100.00', seller=self.user
        )
        self.assertEqual(type(product), Product)
        self.assertEqual(product.title, 'new title')
        self.assertEqual(product.description, 'new desc')
        self.assertEqual(product.price, Decimal('100.00'))
        self.assertEqual(product.seller, self.user)

    def test_delete(self):
        self.service.delete(self.product.pk)
        all_products = self.service.get_all()
        self.assertEqual(len(all_products), 0)

