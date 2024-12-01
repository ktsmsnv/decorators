import datetime
from decorators import MessageDec
from interface.message import Message


class DateDec(MessageDec):
    #декоратор добавления даты в конец сообщения

    def __init__(self, date: datetime.date, message: Message):
        #инициализация
        super().__init__(message)
        self._message = message
        self._date = self._get_date(date)

    def _get_date(self, date: datetime.date) -> str:
        #приведение даты к формату
        return date.strftime("%d.%m.%Y")

    def _get_content(self) -> str:
        #возврат сообщения
        return f"{self._message._get_content()}\n{self._date}"
