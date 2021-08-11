"""
- Para enviar arquivos binários a um servidor de e-mail projetado para trabalhar com dados textuais,
eles precisam ser codificados antes do transporte. Isso é mais comumente feito usando o base64,
que codifica dados binários em caracteres ASCII imprimíveis.

O exemplo de código abaixo mostra como enviar um e-mail com um arquivo PDF como anexo:
"""

import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Um e-mail com anexo de Python"
body = "Este é um e-mail com anexo enviado de Python"

# Usuário informa os dados para acessar o seu email (Bol)
sender_email = input('Digite seu email: ')
receiver_email = input('Digite o email de destino: ')
password = input("Digite a senha: ")

# Crie uma mensagem multiparte e defina cabeçalhos
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "imagem.png"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Adicionar arquivo como application / octet-stream
    # O cliente de e-mail geralmente pode baixar isso automaticamente como anexo
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Codifique o arquivo em caracteres ASCII para enviar por e-mail
encoders.encode_base64(part)

# Adicionar cabeçalho como par chave / valor à parte do anexo
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Adicionar anexo à mensagem e converter mensagem em string
message.attach(part)
text = message.as_string()

# Faça login no servidor usando contexto seguro e envie e-mail
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtps.bol.com.br", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
