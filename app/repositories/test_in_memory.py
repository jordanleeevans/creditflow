from pydantic import BaseModel

from repositories.in_memory import InMemoryRepository


class Record(BaseModel):
    name: str


def test_save_stores_record_by_key_and_returns_it():
    repo = InMemoryRepository[int, Record]()
    record = Record(name="John Doe")

    result = repo.save(1, record)

    assert result == record
    assert repo.db == {1: record}


def test_get_returns_record_for_key():
    repo = InMemoryRepository[int, Record]()
    record = Record(name="John Doe")
    repo.save(1, record)

    result = repo.get(1)

    assert result == record


def test_get_returns_none_for_missing_key():
    repo = InMemoryRepository[int, Record]()

    result = repo.get(1)

    assert result is None
