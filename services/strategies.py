from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import UUID

from django.db.models import Model, QuerySet
from django.shortcuts import get_object_or_404


class BaseCRUDStrategy(ABC):
    """Base class for CRUD Strategies with default interface

    Methods
    -------
    get_concrete(*args, **kwargs)
        Return a concrete entry
    get_all(*args, **kwargs)
        Return all entries
    update(*args, **kwrags)
        Update a concrete entry
    create(*args, **kwargs)
        Create a new entry
    delete(*args, **kwargs)
        Delete an entry

    """

    def __init__(self, model: Model) -> None:
        self._model = model

    @abstractmethod
    def get_concrete(self, *args, **kwargs):
        """Return a concrete entry"""
        pass

    @abstractmethod
    def get_all(self, *args, **kwargs):
        """Return all entries"""
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        """Update a concrete entry"""
        pass

    @abstractmethod
    def create(self, *args, **kwargs):
        """Create a new entry"""
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        """Delete an entry"""
        pass


class SimpleCRUDStrategy(BaseCRUDStrategy):
    """CRUD Strategy with simple default functionality"""

    def get_concrete(self, pk: UUID) -> Model:
        """Return a concrete entry with pk"""
        entry = get_object_or_404(self._model, pk=pk)
        return entry

    def get_all(self) -> QuerySet:
        """Return all entries"""
        entries = self._model.objects.all()
        return entries

    # TODO: Fix this method
    def update(self):
        pass

    # TODO: Fix this method
    def create(self):
        pass

    def delete(self, pk):
        """Delete a concrete entry with pk"""
        entry = self.get_concrete(pk)
        entry.delete()

