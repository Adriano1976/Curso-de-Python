"""
- MIMEMultipart - É usado como padrão da mensagem para identificar o destinatário e a origem do email.
- MIMEText - É usado como padrão para identificar o corpo do e-mail com um texto comum, texto em
html ou uma imagem.
- MIMEImagem - É usado como padrão para enviar imagens em anexo no email a ser enviado.
- smtplib - É usado como padrão para conectar o programa em python ao servidor de email.
- attach - É usado para enviar o corpo da mensagem em texto ou em html e ainda anexar uma imagem.
- smtplib.SMTP - É usado para identificar o host e a porta do provedor do email.
- smtp.ehlo() - É usado para informar ao servidor que vai enviar uma mensagem.
- smtp.starttls() - É usado para reforçar a segurança na hora do envio da mensagem.
- smtp.login - É usado para identificar o email e a senha do usuário que está enviando a mensagem.
- smtp.send_message() - É usado para enviar a mensagem.
"""

import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

# Usuário informa os dados para acessar o seu email (Gmail)
user = input('Informe seu Email: ')
password = input("Informe sua senha: ")
name = input('Informe seu nome: ')

with open('Template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome=name, data=data_atual)

msg = MIMEMultipart()
msg['from'] = name
msg['to'] = user
msg['subject'] = 'Atenção: este é um e-mail de textes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)
        print('\nE-mail enviado com sucesso.')
    except Exception as e:
        print('\nE-mail não enviado...')
        print('Erro:', e)
