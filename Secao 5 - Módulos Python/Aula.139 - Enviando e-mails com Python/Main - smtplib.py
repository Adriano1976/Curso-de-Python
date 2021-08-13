import smtplib

subject = 'message subject'

smtpserver = smtplib.SMTP("smtp.live.com", port=25)

# Usuário informa os dados para acessar o seu email (Hotmail)
sender = input('Informe seu email: ')
password = input("Informe sua senha: ")
to = input('Informe o email de destino: ')

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(sender, password)
header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
message = header + '\n This is my message'
smtpserver.sendmail(sender, to, message)
smtpserver.close()
print('Email enviado com sucesso.')
