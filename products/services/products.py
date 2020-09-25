from __future__ import annotations
from uuid import UUID
from typing import Any

from django.db.models import QuerySet, Model
from django.forms import Form

from services import BaseCRUDService
from ..models import Product
from ..forms import ProductForm
from .reviews import ReviewService


class ProductService(BaseCRUDService):
    """Service with business logic for products

    Attributes
    ----------
    model : Model
        Product model
    form : Form
        Product form
    review_service
        Service to work with reviews

    Methods
    -------
    get_reviews(product_pk)
        Return reviews of product
    add_review(product_pk, **data)
        Add new review for product
    remove_review(review_pk)
        Remove a review

    """

    model = Product
    form = ProductForm
    review_service = ReviewService()

    def get_reviews(self, product_pk: UUID) -> QuerySet:
        """Return reviews of product with product_pk"""
        product = self.get_concrete(product_pk)
        reviews = product.reviews.all()
        return reviews

    def add_review(self, product_pk: UUID, **data) -> Any[Form, Model]:
        """Add new review for product with product_pk"""
        product = self.get_concrete(product_pk)
        response = self.review_service.create(product=product, **data)
        return response

    def remove_review(self, review_pk: UUID) -> None:
        """Remove a review with pk"""
        self.review_service.delete(review_pk)

