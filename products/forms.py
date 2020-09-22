from django import forms

from .models import Product, Review


class ProductForm(forms.Form):
    """Form for creating/updating products

    Attributes
    ----------
    title : CharField
        Title of product
    description : CharField
        Description of product
    price : DecimalField
        Price of product

    """

    title = forms.CharField(max_length=255)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)


class ReviewForm(forms.Form):
    """Form for creating/updating reviews

    Attributes
    ----------
    text : CharField
        Text of review
    rating : IntegerField
        Product rating

    """

    text = forms.CharField()
    rating = forms.IntegerField(max_value=5, min_value=0)

