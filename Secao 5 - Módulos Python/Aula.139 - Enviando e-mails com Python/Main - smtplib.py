import smtplib

subject = 'message subject'

smtpserver = smtplib.SMTP("smtps.bol.com.br", 587)

# Usuário informa os dados para acessar o seu email (Bol)
sender = input('Informe seu email: ')
user = input('Informe seu nome de usuário: ')
password = input("Informe sua senha: ")
to = input('Informe o email de destino: ')

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(user, password)
header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
message = header + '\n This is my message'
smtpserver.sendmail(sender, to, message)
smtpserver.close()
