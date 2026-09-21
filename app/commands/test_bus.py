import pytest

from commands.actions import Command
from commands.bus import CommandBus
from handlers.base import Handler


class ExampleCommand(Command):
    value: int


class ExampleHandler(Handler[ExampleCommand]):
    def handle(self, command: ExampleCommand) -> int:
        return command.value * 2


def test_dispatch_routes_command_to_registered_handler():
    bus = CommandBus()
    bus.register(ExampleCommand, ExampleHandler())

    result = bus.dispatch(ExampleCommand(value=3))

    assert result == 6


def test_dispatch_rejects_unregistered_command():
    bus = CommandBus()

    with pytest.raises(ValueError, match="Invalid command"):
        bus.dispatch(ExampleCommand(value=3))
