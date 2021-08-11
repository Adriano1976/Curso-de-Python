import smtplib
import ssl


port = 465  # For SSL
user = input('Informe seu Email: ')
password = input("Informe sua senha: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtps.bol.com.br", port, context=context) as server:
    server.login(user, password)
    # TODO: Send email here
