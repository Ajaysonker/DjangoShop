import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator


User = get_user_model()


class Product(models.Model):
    """Product model

    Attributes
    ----------
    uuid : UUIDField
        UUID primary key
    title : CharField
        Title of product
    description : TextField
        Description of product
    price : DecimalField
        Price of product
    seller : ForeignKey
        Seller that sells the product
    pub_date : DateField
        Product published date

    """
    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title[:50]


class Review(models.Model):
    """Review model

    Attributes
    ----------
    uuid : UUIDField
        UUID primary key
    text : TextField
        Text of review
    product : ForeignKey
        Product that review for
    rating : PositiveIntegerField
        Rating of product
    author : ForeignKey
        Author of review
    pub_date : DateField
        Review published date

    """

    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4
    )
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text[:50]

