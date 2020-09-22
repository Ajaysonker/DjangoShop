from abc import ABC

from django.core.exceptions import ImproperlyConfigured

from .strategies import SimpleCRUDStrategy


class BaseCRUDService(ABC):
    """Base class with CRUD functionality

    Attributes
    ----------
    crud_strategy
        Strategy with CRUD realisation
    model : Model
        Model service work with

    Methods
    -------
    get_concrete(*args, **kwargs)
        Return a concrete entry
    get_all(*args, **kwargs)
        Return all entries
    update(*args, **kwargs)
        Update an entry
    create(*args, **kwargs)
        Create an entry
    delete(*args, **kwargs)
        Delete an entry

    """

    crud_strategy = SimpleCRUDStrategy
    model = None
    form = None

    def __init__(self) -> None:
        if not all((self.model, self.form)):
            raise ImproperlyConfigured(
                f"You need to set `crud_strategy`, `model`"
                "and `form` attributes"
            )

        self._strategy = self.crud_strategy(self.model, self.form)

    def get_concrete(self, *args, **kwargs):
        """Return a concrete entry"""
        return self._strategy.get_concrete(*args, **kwargs)

    def get_all(self, *args, **kwargs):
        """Return all entries"""
        return self._strategy.get_all(*args, **kwargs)

    def update(self, *args, **kwargs):
        """Update an entry"""
        return self._strategy.update(*args, **kwargs)

    def create(self, *args, **kwargs):
        """Create a new entry"""
        return self._strategy.create(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Delete an entry"""
        return self._strategy.delete(*args, **kwargs)

