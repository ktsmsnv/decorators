import unittest
import datetime

import decorators.date
import interface.message


class TestDate(unittest.TestCase):
    #проверка добавления даты

    def setUp(self):
        #первоначальные значения
        self.message = interface.message.Message("Test message")
        self.date = datetime.date.today()
        self.message_with_date = (
            f"Test message\n{datetime.date.today().strftime('%d.%m.%Y')}"
        )
        self.message_with_date_decorator = decorators.date.DateDec(
            self.date, self.message
        )

    def test_header(self):
        #сравнение содержимого сообщений
        self.assertEqual(
            self.message_with_date, self.message_with_date_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
