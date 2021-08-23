from config import sender, password, recipients, smtp_server, mail_subject
from config import currencies, header, file_path
from browser import Browser
from ExcelOpenPyXl import write_array_to_excel, prepear_data_to_excel, check_cell_type, auto_fit
from Mail import Mail, MailSender, get_count
from Logger import log


def main():
    """ инициализация парсера и парсинг сайта """
    browser = Browser()
    currencies_dict = browser.get_all_currency_rate(currencies)

    """ подготовка данных для записи в таблтицу """
    table_content, line_count = prepear_data_to_excel(currencies_dict["USD/RUB"],
                                                      currencies_dict["EUR/RUB"], header)

    """ запись данных в excel файл """
    write_array_to_excel(table_content)

    """ проверка формата ячеек """
    check_cell_type(file_pah=file_path)

    """ Выравнивание ширины столбцов """
    auto_fit()

    """ подготовка сообщения и почтового сервера """
    mail = Mail(recipients, sender, mail_subject,
                f"В файле {get_count(line_count)}.", file_path)

    mail_sender = MailSender(sender, password, smtp_server)

    """ отправка письма и запись лога """
    mail_sender.send_mail(mail)
    log("Main", "Running successful!")


if __name__ == '__main__':
    main()
