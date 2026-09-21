from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(ABC, Generic[T]):
    def __init__(self, db: object) -> None:
        self.db = db

    @abstractmethod
    def save(self, data: T) -> T:
        raise NotImplementedError
