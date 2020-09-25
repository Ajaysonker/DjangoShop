from services import BaseCRUDService
from ..models import Review
from ..forms import ReviewForm


class ReviewService(BaseCRUDService):
    """Service with business logic for reviews

    Attributes
    ----------
    model : Model
        Review model
    form : Form
        Review form

    """

    model = Review
    form = ReviewForm

