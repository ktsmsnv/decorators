class Message:
    #интерфейс базового сообщения

    def __init__(self, message: str):
      #инициализация сообщения
        self._message = message

    def _get_content(self) -> str:
        #возврат значения объекта
        return self._message

    def print(self) -> None:
        #вывод сообщения в консоль
        print(self._get_content())
