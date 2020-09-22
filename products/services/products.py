from services import BaseCRUDService

from ..models import Product
from ..forms import ProductForm


class ProductService(BaseCRUDService):
    """Service with business logic for products

    Attributes
    ----------
    model : Model
        Product model
    form : Form
        Product form

    """

    model = Product
    form = ProductForm

