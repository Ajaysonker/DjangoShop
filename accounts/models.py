"""User models"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    """Base user with checking is he/she a seller

    Attributes
    ----------
    is_seller : BooleanField
        True if user is seller

    """

    is_seller = models.BooleanField('seller status', default=False)

