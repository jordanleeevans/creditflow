import logging
from typing import Any

from commands.actions import Command
from handlers.base import Handler
from logging_config import log_extra

logger = logging.getLogger(__name__)


class CommandBus:
    def __init__(self) -> None:
        self._registry: dict[type[Command], Handler[Any]] = {}

    def register(self, command_type: type[Command], handler: Handler[Any]) -> None:
        self._registry[command_type] = handler
        logger.info(
            "Registered command handler",
            **log_extra(
                event="command_handler_registered",
                command=command_type.__name__,
                handler=handler.type(),
            ),
        )

    def dispatch(self, command: Command) -> Any:
        command_type = type(command)
        logger.info(
            "Dispatching command",
            **log_extra(
                event="command_dispatch_started",
                command=command_type.__name__,
            ),
        )
        if command_type not in self._registry:
            logger.warning(
                "Command dispatch failed",
                **log_extra(
                    event="command_dispatch_failed",
                    command=command_type.__name__,
                    reason="unregistered_command",
                ),
            )
            raise ValueError(
                f"Invalid command, expected one of "
                f"{[cmd.__name__ for cmd in self._registry]}."
            )
        handler = self._registry[command_type]
        result = handler.handle(command)
        logger.info(
            "Command dispatched",
            **log_extra(
                event="command_dispatch_completed",
                command=command_type.__name__,
                handler=handler.type(),
                result=type(result).__name__,
            ),
        )
        return result
