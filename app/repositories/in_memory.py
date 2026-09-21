from typing import Generic, MutableMapping, Protocol, TypeVar

from repositories.base import Repository


class HasId(Protocol):
    id: int


T = TypeVar("T", bound=HasId)


class InMemoryRepository(Repository[T], Generic[T]):
    def __init__(self, db: MutableMapping[int, T] | None = None) -> None:
        self.db: MutableMapping[int, T] = db if db is not None else {}

    def save(self, data: T) -> T:
        self.db[data.id] = data
        return data
