import base64
import datetime
import unittest

import decorators
import interface


class TestAllDecorators(unittest.TestCase):
    #проверка полной цепочки декораторов

    def setUp(self):
        #создание тестового сообщения
        self.test_message = "Заголовок\nСообщение\nПодпись\n31.12.2024"
        #создание полной цепочки декораторов
        message = interface.message.Message("Сообщение")
        message_with_header = decorators.HeaderDec("Заголовок", message)
        message_with_header_footer = decorators.FooterDec(
            "Подпись", message_with_header
        )
        self.message_with_header_footer_date = decorators.DateDec(
            datetime.date(2024, 12, 31), message_with_header_footer
        )
        #кодирование получившегося сообщения в Base64
        self.message_with_header_footer_date_base64 = decorators.Base64(
            self.message_with_header_footer_date
        )

    def test_all_decorators(self):
        #проверка соответствия полной цепочки декораторов
        self.assertEqual(self.test_message, self.message_with_header_footer_date._get_content())
        #проверка кодирования
        self.assertEqual(
            base64.b64encode(self.test_message.encode("utf-8")).decode("utf-8"),
            self.message_with_header_footer_date_base64._get_content(),
        )


if __name__ == "__main__":
    unittest.main()
