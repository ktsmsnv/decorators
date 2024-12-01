import base64

from decorators import MessageDec
from interface.message import Message


class Base64(MessageDec):
    #декоратор кодирования сообщения в Base64

    def __init__(self, message: Message):
        #инициализация декоратора

        super().__init__(message)
        self._message = message
        self._base64 = self._get_base64()

    def _get_content(self) -> str:
        #возврат сообщения
        return self._base64

    def _get_base64(self) -> str:
        #кодирование в Base64
        return base64.b64encode(self._message._get_content().encode("utf-8")).decode(
            "utf-8"
        )
