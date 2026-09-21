from typing import Generic, MutableMapping, TypeVar

from repositories.base import Repository

K = TypeVar("K")
T = TypeVar("T")


class InMemoryRepository(Repository[K, T], Generic[K, T]):
    def __init__(self, db: MutableMapping[K, T] | None = None) -> None:
        self.db: MutableMapping[K, T] = db if db is not None else {}

    def save(self, key: K, data: T) -> T:
        self.db[key] = data
        return data

    def get(self, key: K) -> T | None:
        return self.db.get(key)
