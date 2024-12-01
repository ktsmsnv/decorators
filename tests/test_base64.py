import unittest
import base64

import decorators.base64
import interface.message


class TestBase64(unittest.TestCase):
   #проверка кодирования в Base64

    def setUp(self):
        #первоначальные значения
        self.message = interface.message.Message("Test message")
        self.message_with_base64 = base64.b64encode(
            "Test message".encode("utf-8")
        ).decode("utf-8")
        self.message_with_base64_decorator = (
            decorators.base64.Base64(self.message)
        )

    def test_header(self):
        #cравнение содержимого сообщений
        self.assertEqual(
            self.message_with_base64, self.message_with_base64_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
