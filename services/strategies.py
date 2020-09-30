from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Any

from django.db.models import Model, QuerySet
from django.forms import Form
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


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

    def __init__(self, model: Model, form: Form) -> None:
        self._model = model
        self._form = form

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
    """CRUD Strategy with simple default functionality

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

    def get_concrete(self, pk: UUID) -> Model:
        """Return a concrete entry with pk"""
        entry = get_object_or_404(self._model, pk=pk)
        return entry

    def get_all(self) -> QuerySet:
        """Return all entries"""
        entries = self._model.objects.all()
        return entries

    def _check_is_data_valid(self, data: dict) -> None:
        """Check is data valid"""
        fields = [
            field.name for field in self._model._meta.get_fields()
            if field.editable
        ]
        if list(data.keys()).sort() != fields.sort():
            raise ValueError(
                f"Data is incorrect: {list(data.keys()).sort()} "
                "!= {fields.sort(0)}"
            )

    def update(self, pk: UUID, **data) -> Any[Model, Form]:
        """Update a concrete entry with pk from data"""
        form = self._form(data)
        entry = self.get_concrete(pk)
        if form.is_valid():
            for field, value in form.cleaned_data.items():
                setattr(entry, field, value)

            entry.save()
            return entry

        return form

    def create(self, **data) -> Any[Model, Form]:
        """Create a new entry from data"""
        form = self._form(data)
        if form.is_valid():
            self._check_is_data_valid(data)
            entry = self._model.objects.create(**data)
            return entry

        return form

    def delete(self, pk: UUID) -> None:
        """Delete a concrete entry with pk"""
        entry = self.get_concrete(pk)
        entry.delete()

