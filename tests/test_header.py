import unittest

import decorators.header
import interface.message


class TestHeader(unittest.TestCase):
    #проверка добавления заголовка

    def setUp(self):
        #первоначальные значения
        self.header = "Header"
        self.message = interface.message.Message("Test message")
        self.message_with_header = "Header\nTest message"
        self.message_with_header_decorator = (
            decorators.header.HeaderDec(self.header, self.message)
        )

    def test_header(self):
        #cравнение содержимого сообщений
        self.assertEqual(
            self.message_with_header, self.message_with_header_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
