# TODO: Create tests for ProductService
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models import Model

from .models import Product, Review
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
        self.review = Review.objects.create(
            text='test_review', product=self.product,
            rating=5, author=self.user
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

    def test_get_review(self):
        reviews = self.service.get_reviews(self.product.pk)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0], self.review)

    def test_add_review(self):
        new_review = self.service.add_review(
            self.product.pk, text="new_review",
            rating=5, author=self.user
        )
        self.assertIsInstance(new_review, Model)
        self.assertEqual(new_review.text, "new_review")
        self.assertEqual(new_review.product, self.product)
        self.assertEqual(new_review.rating, 5)
        self.assertEqual(new_review.author, self.user)

    def test_remove_review(self):
        self.service.remove_review(self.review.pk)
        all_reviews = self.service.get_reviews(self.product.pk)
        self.assertEqual(len(all_reviews), 0)

