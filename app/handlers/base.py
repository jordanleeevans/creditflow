from abc import ABC, abstractmethod
from typing import Any
from typing import Generic, TypeVar

from commands.actions import Command

C = TypeVar("C", bound=Command)


class Handler(ABC, Generic[C]):
    @abstractmethod
    def handle(self, command: C) -> Any:
        raise NotImplementedError

    def type(self) -> str:
        return "missing"
