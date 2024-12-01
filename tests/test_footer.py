import unittest

import decorators.footer
import interface.message


class TestFooter(unittest.TestCase):
    #проверка добавления подписи

    def setUp(self):
        #первоначальные значения
        self.message = interface.message.Message("Test message")
        self.footer = "Footer"
        self.message_with_footer = "Test message\nFooter"
        self.message_with_footer_decorator = (
            decorators.footer.FooterDec(self.footer, self.message)
        )

    def test_header(self):
        #сравнение содержимого сообщений
        self.assertEqual(
            self.message_with_footer, self.message_with_footer_decorator._get_content()
        )


if __name__ == "__main__":
    unittest.main()
