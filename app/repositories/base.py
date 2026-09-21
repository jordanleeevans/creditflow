from abc import ABC, abstractmethod
from typing import Generic, TypeVar

K = TypeVar("K")
T = TypeVar("T")


class Repository(ABC, Generic[K, T]):
    def __init__(self, db: object) -> None:
        self.db = db

    @abstractmethod
    def save(self, key: K, data: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: K) -> T | None:
        raise NotImplementedError
