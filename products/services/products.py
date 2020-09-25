from uuid import UUID
from typing import Any

from django.db.models import QuerySet

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
    get_reviews(pk)
        Return reviews of product
    add_review(pk, **data)
        Add new review for product
    remove_review(pk)
        Remove a review

    """

    model = Product
    form = ProductForm
    review_service = ReviewService()

    def get_reviews(self, pk: UUID) -> QuerySet:
        """Return reviews of product with pk"""
        product = self.get_concrete(pk)
        reviews = product.reviews.all()
        return reviews

    def add_review(self, pk: UUID, **data) -> Any[Form, Model]:
        """Add new review for product with pk"""
        product = self.get_concrete(pk)
        review = self.review_service.create(product=product, **data)
        return review

    def remove_review(self, pk: UUID) -> None:
        """Remove a review with pk"""
        self.review_service.delete(pk)

