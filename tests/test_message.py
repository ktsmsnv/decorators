import unittest

import interface.message


class TestMessage(unittest.TestCase):
    #проверка создания сообщения

    def setUp(self):
        #первоначальные значения
        self.message = "Test message"
        self.message_decorator = interface.message.Message(self.message)

    def test_creating_message(self):
        #cравнение содержимого сообщений
        self.assertEqual(self.message_decorator._get_content(), self.message)


if __name__ == "__main__":
    unittest.main()
