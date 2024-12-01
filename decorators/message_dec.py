from interface.message import Message


class MessageDec(Message):
    #базовый декоратор

    def __init__(self, message: Message):
        #инициализация декоратора
        super().__init__(message._get_content())
        self._message = message

    def _get_content(self) -> str:
        #возвращает сообщение
        return self._message._get_content()
