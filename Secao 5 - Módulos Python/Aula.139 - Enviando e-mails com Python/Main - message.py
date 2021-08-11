import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtps.bol.com.br"

# Usuário informa os dados para acessar o seu email (Bol)
sender_email = input('Informe seu email: ')  # Enter your address
receiver_email = input('Informe o email destinatário: ') # Enter receiver address
password = input("Informe sua senha: ")
message = """\
Subject: Hi there
This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

