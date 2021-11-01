import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.live.com"

# Usuário informa os dados para acessar o seu email (Hotmail)
sender_email = input('Informe seu email: ')  # Enter your address
password = input("Informe sua senha: ")
receiver_email = input('Informe o email destinatário: ')  # Enter receiver address

message = """\
Assunto: Olá
Esta mensagem é enviada de Python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('Email enviado com sucesso.')
