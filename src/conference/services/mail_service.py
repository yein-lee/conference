import smtplib
from email.message import EmailMessage


class MailService:
    @classmethod
    def build_password_message(cls, to, new_password) -> EmailMessage:
        message = EmailMessage()
        message['Subject'] = "Dualtalk 3.0 임시 비밀번호 발송"
        message['From'] = "Dualtalk@dualtalk.ai"
        message['To'] = to
        message.set_content("""\
                임시 비밀번호는 {password} 입니다.
                """.format(password=new_password))
        return message

    @classmethod
    def send(cls, message: EmailMessage) -> None:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("Dualtalk@dualtalk.ai", "password")
            smtp.send_message(message)
