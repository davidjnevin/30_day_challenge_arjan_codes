from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Callable


class MessageType(StrEnum):
    TICKET_BOOKED = auto()
    EVENT_CREATED = auto()


@dataclass
class Message:
    message_type: MessageType
    message: str = ""
    data: object | None = None

MessageHandleFn = Callable[[Message], None]


@dataclass
class MessageSystem:
    handlers: dict[MessageType, list[MessageHandleFn]] = field(default_factory=dict)

    def attach(self, message_type: MessageType, handler: MessageHandleFn):
        if type not in self.handlers:
            self.handlers[message_type] = []
        self.handlers[message_type].append(handler)

    def detach(self, message_type: MessageType, handler: MessageHandleFn):
        if type not in self.handlers:
            return
        self.handlers[message_type].remove(handler)

    def post(self, event: Message):
        message_type = event.message_type
        if message_type not in self.handlers:
             return
        for handler in self.handlers[message_type]:
            handler(event)

