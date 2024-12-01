from decorators.message_dec import MessageDec
from interface.message import Message


class HeaderDec(MessageDec):
    #декоратор добавления заголовка в начало сообщения

    def __init__(self, header: str, message: Message):
        #инициализация

        super().__init__(message)
        self._message = message
        self._header = header

    def _get_content(self) -> str:
        #возврат сообщения
        return f"{self._header}\n{self._message._get_content()}"
