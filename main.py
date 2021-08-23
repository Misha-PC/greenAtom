from config import sender, password, recipients, smtp_server, mail_subject
from config import currencies, header, file_path
from browser import Browser
from ExcelOpenPyXl import write_array_to_excel, prepear_data_to_excel, check_cell_type
from ExcelOpenPyXl import CellFromatError, NoSheetError
from Mail import Mail, MailSender, get_count
from Logger import log


def main():
    """ init robot & pars tables """
    browser = Browser()
    currencies_dict = browser.get_all_currency_rate(currencies)

    # prepare table content
    table_content, line_count = prepear_data_to_excel(currencies_dict["USD/RUB"],
                                                      currencies_dict["EUR/RUB"], header)

    """write table content to file"""
    write_array_to_excel(table_content, file_path=file_path)

    """check cell format"""
    try:
        check_cell_type(file_pah=file_path)
    except CellFromatError:
        exit()
    except NoSheetError:
        exit()

    """prepare mail & sender"""
    mail = Mail(recipients, sender, mail_subject,
                f"В файле {get_count(line_count)}.", file_path)

    mail_sender = MailSender(sender, password, smtp_server)

    """send mail"""
    mail_sender.send_mail(mail)

    """ Write log """
    log("Main", "Running successful!")


if __name__ == '__main__':
    main()
