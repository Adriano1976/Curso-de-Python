import smtplib
import ssl

smtp_server = "smtps.bol.com.br"
port = 587  # For starttls
# Usuário informa os dados para acessar o seu email (Bol)
user_email = input('Informe seu Email: ')
password = input("Informe sua senha: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(user_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

