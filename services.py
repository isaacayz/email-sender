import smtplib
from email.message import EmailMessage
from typing import Any


class EmailService:
    def __init__(self, smtp_server: str, port: int, email: str, password: str) -> None:
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.password = password

    def send_message(self, to_email: str, subject: str, body: str) -> None:
        msg = EmailMessage()
        #msg.add_header('From', 'godisgood@vatebra.com')
        msg.set_content(body)
        msg['Subject'] = subject
        msg['TO'] = to_email
        #msg['FROM'] = 'godisgood@vatebra.com'

        with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
            server.login(self.email, self.password)
            server.send_message(msg, self.email)
            pass
        print('Email sent successfully!')

