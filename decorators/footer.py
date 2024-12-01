from decorators import MessageDec
from interface.message import Message


class FooterDec(MessageDec):
    #декоратор добавления подписи в конец сообщения

    def __init__(self, footer: str, message: Message):
       #инициализация

        super().__init__(message)
        self._message = message
        self._footer = footer

    def _get_content(self) -> str:
        #возврат сообщения
        return f"{self._message._get_content()}\n{self._footer}"
