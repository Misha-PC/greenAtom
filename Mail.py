from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import admin_mails, sender, password, smtp_server
import smtplib
import os


class Mail:
    def __init__(self, recipients: list, sender: str,
                 subject: str, body: str, file_path: str = None):

        """
        :param recipients: list recipients
        :param sender:     str  sender email
        :param subject:    str  message subject
        :param body:       str  message text
        :param file_path:  str  [full path to file]
        """

        text = MIMEText(body, 'plain')

        # prepare message
        msg = MIMEMultipart()
        msg["From"] = f"Python script  <{sender}>"
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject
        msg.attach(text)

        # get file info
        if file_path:
            basename = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)

            # load & prepare file to send
            file = MIMEBase('application', f"octet-stream; name={basename}")
            file.set_payload(open(file_path, 'rb').read())
            file.add_header('Content-Discription', basename)
            file.add_header('Content-Discription', f"attachment; filename={basename}; size={file_size}")
            encoders.encode_base64(file)
            msg.attach(file)

        # save message to mail object
        self.msg = msg

    def get_message(self) -> MIMEMultipart:
        return self.msg


class MailSender:
    def __init__(self, sender: str, password: str, smtp_serrver: str):
        self.server = smtplib.SMTP_SSL(smtp_serrver)  # Создаем объект SMTP
        self.server.login(sender, password)           # Авторизируемся на smtp сервере

    def send_mail(self, mail: Mail):
        try:
            self.server.send_message(mail.get_message())
        except Exception as e:
            print(e)
            return False
        return True

    def __del__(self):
        print(f"{self} deleted.")
        # self.server.quit()


def send_mail_to_admins(text: str):
    MailSender(sender, password, smtp_server).send_mail(
        Mail(admin_mails, sender, "Python script: fatal error!", text)
    )


def get_count(c):
    word = ['строка', 'строки', 'строк']
    last_two = int(str(c)[-2:])
    if last_two == 0:
        return f"{c} {word[2]}"
    elif last_two == 1:
        return f"{c} {word[0]}"
    elif last_two < 5:
        return f"{c} {word[1]}"
    elif last_two > 20:
        second = last_two % 10
        if second == 1:
            return f"{c} {word[0]}"
        elif second in [2, 3, 4]:
            return f"{c} {word[1]}"
    return f"{c} {word[2]}"
