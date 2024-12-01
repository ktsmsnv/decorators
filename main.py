import datetime
import decorators
import interface

if __name__ == "__main__":
    #вывод сообщения
    message = interface.message.Message("Проверьте, пожалуйста, ваш почтовый ящик.")
    message.print()
    print()

    #добавление заголовка
    message_header = decorators.header.HeaderDec(
        "Добрый день!", message
    )
    message_header.print()
    print()

    #добавление подписи
    message_footer = decorators.footer.FooterDec(
        "С уважением, администрация сайта.", message_header
    )
    message_footer.print()
    print()

    #добавление даты
    message_date = decorators.date.DateDec(
        datetime.date.today(), message_footer
    )
    message_date.print()
    print()

    #кодирование сообщения в Base64
    message_base64 = decorators.base64.Base64(message_date)
    message_base64.print()
    print()
