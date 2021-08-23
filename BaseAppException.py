from Logger import log
from Mail import send_mail_to_admins


class BaseAppException(Exception):
    """
        Базовое исключение, необходимо для того, что бы при возникновении
        любого из его наследников ошибка автоматически записывалась
        в лог и отправлялась разработчикам на почту.
    """
    def __init__(self, message, *args, **kwargs):
        self.message = message
        if kwargs:
            self.msgExt = str()
            for key in kwargs.keys():
                self.msgExt += f"\t{key}: {kwargs[key]}.\n"
        source = "Error"
        if "func" in kwargs.keys():
            source = kwargs["func"]

        log(source, self.message)
        send_mail_to_admins(self.message)
