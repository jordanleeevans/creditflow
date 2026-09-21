from typing import Any

from commands.actions import Command
from handlers.base import Handler


class CommandBus:
    def __init__(self) -> None:
        self._registry: dict[type[Command], Handler[Any]] = {}

    def register(self, command_type: type[Command], handler: Handler[Any]) -> None:
        self._registry[command_type] = handler

    def dispatch(self, command: Command) -> Any:
        command_type = type(command)
        if command_type not in self._registry:
            raise ValueError(
                f"Invalid command, expected one of "
                f"{[cmd.__name__ for cmd in self._registry]}."
            )
        handler = self._registry[command_type]
        return handler.handle(command)
