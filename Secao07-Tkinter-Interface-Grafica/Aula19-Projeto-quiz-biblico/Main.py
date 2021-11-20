from tkinter import *


# Método referente a pergunta --------------------------------------------------------------
def daniel_116():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="Para que país Daniel foi levado como escravo?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Babilônia",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1116_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Egito",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2116_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Assíria",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2116_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Israel",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2116_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1116_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nDaniel 1:1-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2116_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nDaniel 1:1-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------------

# Método de tiago referente a pergunta

def tiago_514():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="Com o que devemos ungir os enfermos?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Água",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2514_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Azeite",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1514_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Vinho",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2514_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Essência",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2514_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1514_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nTiago 5:14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2514_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nTiago 5:14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def geneses_4125():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="Quem eram os pais de Caim, Abel e Sete?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Isaque e Rebeca",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt24125_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Davi e Mical",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt24125_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Adão e Eva",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt14125_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Maria e Jó",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt24125_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt14125_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nGênesis 4:1-25',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt24125_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nGênesis 4:1-25',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joao_148():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="Que discípulo Jesus encontrou debaixo da figueira?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Natanael",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1148_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Mateus",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2148_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Judas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2148_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Zaqueu",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2148_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1148_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 1:48',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2148_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 1:48',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def atos_182():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="Quem foi o imperador romano que \nobrigou todos os judeus a saírem de Roma?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Otávio",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2182_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Augusto",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2182_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Cláudio",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1182_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Constantino",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2182_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1182_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nAtos 18:2',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2182_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nAtos 18:2',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def Isamuel_174950():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="O que Davi utilizou para matar Golias?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Um dardo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2174950_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Arco e flecha",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2174950_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Uma funda",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1174950_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Uma pedra",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2174950_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1174950_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nI Samuel 17:49-50',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2174950_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nI Samuel 17:49-50',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def lucas_323():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quandos anos tinha Jesus Cristo \nquando comerçou a pregar seu ministério?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Aproximadamente 30 anos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1323_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Aproximadamente 33 anos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2323_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Aproximadamente 35 anos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2323_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Aproximadamente 32 anos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2323_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1323_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nLucas 3:23',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2323_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nLucas 3:23',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def exodo_163():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="No deserto, sobre o que os israelitas \nse queixaram com Moisés e Arão?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Que estava muito quente.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2163_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Que eles estavam cansados.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2163_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Que não havia carne para comer.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1163_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Que não tinha água para beber.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2163_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1163_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nÊxodo 16:3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2163_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nÊxodo 16:3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def marcos_104652():
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
                     text="Perto de qual cidade o cego \nBartimeu foi curado por Jesus Cristo?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Jerusalém.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2104652_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Jericó.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1104652_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Betânia.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2104652_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Belém.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2104652_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1104652_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMarcos 10:46-52',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2104652_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMarcos 10:46-52',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def mateus_41819():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Pedro estava jogando sua rede em que mar \nquando Jesus o chamou para ser seu discípulo?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Mar da Galiléia",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt141819_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Mar Morto",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt241819_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Mar Mediterrâneo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt241819_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Mar Cáspio",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt241819_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt141819_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMateus 4:18-19',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt241819_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMateus 4:18-19',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def josue_6120():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Os muros de que cidade caíram \nquando os israelitas gritaram?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Jerusalém",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt26120_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Jericó",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt16120_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Jizreed",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt26120_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Nazaré",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt26120_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt16120_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJosué 6:1-20',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt26120_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJosué 6:1-20',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joao_121213():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quando Jesus se aproximou de \nJerusalém montado \
em um jumento, \no que as pessoas acenavam para ele",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Ramos de oliveiras",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2121213_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Ramos de palmas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2121213_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Ramos de coqueiros",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2121213_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Ramos de palmeiras",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1121213_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1121213_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 12:12-13',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2121213_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 12:12-13',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def lucas_194548():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Para onde Jesus foi quando ele entrou em Jerusalém\n"
                          "no sengundo dia após seua entrada triunfal?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="O mercado",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2194548_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Os estábulos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2194548_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="O templo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1194548_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="A sinagoga",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2194548_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1194548_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nLucas 19:45-48',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2194548_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nLucas 19:45-48',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joao_1831():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quando Pilatos saiu do Pretório, o que \nele disse aos líderes judeus sobre Jesus",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Que Jesus era inocente.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21831_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Que o julgassem segundo suas leis",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt11831_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Que ele havia libertado Jesus",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21831_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Que ele lavaria as mãos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21831_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt11831_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 18:31',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt21831_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 18:31',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def mateus_2663():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Durante a audiência na casa de Caifás, \no que o \
sumo sacerdócio fez quando \nJesus confessou que era Cristo, o filho de Deus ",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Ordenou que Jesus fosse retirado da sala.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22663_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Esbofeteou Jesus",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22663_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Rasgou suas proprias roupas.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt12663_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Que Jesus deveria ser cruscificado.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22663_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt12663_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMateus 26:63',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt22663_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMateus 26:63',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joao_1932():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quando so soldados se aproximaram de \nJesus e dos dois criminosos, o que eles fizeram?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Quebraram as pernas dos 2 criminosos.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt11932_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Quebraram as pernas de Jesus",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21932_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Perceberam que todos estavam mortes.",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21932_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text='Tiveram medo de quebrar as pernas de Jesus',
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21932_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt11932_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 19:32',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt21932_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 19:32',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def mateus_2730():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Depois de espancado, o que os soldados \nromanos \
fizeram com a cana que haviam \ncolocado na mão de Jesus?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Quebraram seu braço",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22730_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Bateram em sua cabeça",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt12730_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Esmagaram seus dedos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22730_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Bateram em suas costas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22730_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt12730_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMateus 27:30',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt22730_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMateus 27:30',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def geneses_2533():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que Esaú vendeu a seu irmão, Jacó?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Uma benção",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22533_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Seu direito de primogenitura",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt12533_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Carne de cordeiro",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22533_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Seu direito a revelação",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22533_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt12533_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nGêneses 25:33',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt22533_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nGêneses 25:33',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def josue_2432():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quando os ossos de José foram \nretirados do Egito, onde eles \nfinalmente foram enterrados?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Jerusalém",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22432_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Siquém",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt12432_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Belém",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22432_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Israel",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22432_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt12432_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJosué 24:32',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt22432_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJosué 24:32',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joao_1245():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quem se indignou com a ação de \nMaria em ungir Jesus com o bálsamo?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Judas Iscariotes",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt11245_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="O irmão de Maria",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21245_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Lazáro",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21245_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Marta",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21245_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt11245_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 12:4-5',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt21245_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 12:4-5',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def apocalipse_27():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que João viu voando pelo meio \ndo céu deixando uma mensagem?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Pássaro",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt227_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Lúcife",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt227_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Espírito Santo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt227_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Anjo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt127_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt127_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nApocalipse 14:6-7',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt227_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nApocalipse 14:6-7',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def isaias_223():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que Isaías viu sendo estabelecido \nno cume dos montes nos últimos dias?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Tabernáculo de Moisés",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2223_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="A Casa do Senhor",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1223_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="A idade das Trevas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2223_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="As setes igrejas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2223_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1223_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nIsaias 2:2-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2223_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nIsaias 2:2-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joao_467():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual era o nome do poço de onde \n"
                          "a mulher samaritana com quem \n"
                          "Jesus falou estava tirando água?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Poço de Abraão",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2467_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Poço de Jacó",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1467_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Poço de Isaque",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2467_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Poço de Betel",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2467_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1467_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 4:6-7',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2467_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 4:6-7',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def mateus_434():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que o diabo pedio que \nJesus transformasse em pão?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Cobras",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2434_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Pedras",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1434_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Varas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2434_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Moedas de pratas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2434_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1434_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMateus 4:3-4',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2434_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMateus 4:3-4',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def malaquias_3812():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="De que forma o homem rouba a Deus constantemente?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Não pagar os tributos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt23812_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Não ser honesto com o próximo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt23812_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Nos sacrifícios ofertados",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt23812_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Nos dízimos e nas ofertas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt13812_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt13812_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMalaquias 3:8-12',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt23812_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMalaquias 3:8-12',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def Itimoteo_413():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="De que forma ocorrerá a apostasia nos últimos dias?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Muitos pregarão o evangelho",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2413_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Acreditarão na doutrina da fé",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2413_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Perda da fé verdadeira",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1413_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Verdades ensinas pelo homens justos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2413_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1413_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nI Timóteo 4:1-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2413_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nI Timóteo 4:1-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def joel_22832():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que o Senhor promete derramar \nsobre as pessoas nos últimos dias?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Fé e compaixão",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt222832_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Seu Espírito e salvação",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt122832_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Fé e arrependimento",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt222832_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Provação e alegria",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt222832_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt122832_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoel 2:28-32',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt222832_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoel 2:28-32',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def proverbios_151():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="De acordo com Provérbios 15:1, \no que faz uma resposta gentil?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Faz recuar o furor",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1151_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Encoraja a amizade",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2151_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Inicia contendas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2151_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Traz tristesas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2151_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1151_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nProvérbios 15:1',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2151_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nProvérbios 15:1',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def efesios_21920():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Como era conhecido os seguidores \nde Cristo na época do apóstolo Paulo?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Cristãos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt221920_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Filhos espirituais",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt221920_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Considadãos dos santos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt121920_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Discípulos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt221920_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt121920_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nEfésios 2:19-20',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt221920_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nEfésios 2:19-20',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def hebreus_1113():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual o verdadeiro significado da fé?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Alegria",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21113_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Esperança",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21113_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Crença e espiritualidade",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21113_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Certeza e convicção",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt11113_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt11113_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nHebreus 11:1-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt21113_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nHebreus 11:1-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def isaias_118():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual o efeito do arrependimento \ntraz diante do Senhor?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Alegria e saúde",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2118_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Esperança constante",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2118_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Pecado corrigido",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2118_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Perdão dos pecados",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1118_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1118_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nIsaias 1:18',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2118_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nIsaias 1:18',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def Icorintios_214():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Por que nem todas as pessoas \nnão aceite as coisas de Deus?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Porque lhe são loucuras",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1214_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Porque não entende",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2214_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Porque não tem fé",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2214_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Porque não é bom",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2214_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1214_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nI Coríntios 2:14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2214_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nI Coríntios 2:14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def atos_1313():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Como Barnabé e Saulo foram chamados \npara o ministério apostólico?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Em uma votação",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21313_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Por indicações",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21313_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Através de jejum e oração",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt11313_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Por meio da fé coletiva",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt21313_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt11313_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nAtos 13:1-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt21313_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nAtos 13:1-3',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def proverbios_232021():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual foi a advertência contra \na embriaguez, a gula e a preguiça \nescrita neste provérbio?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Tristeza",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2232021_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Pobreza",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1232021_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Perda familiar",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2232021_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Contenação eterna",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2232021_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1232021_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nProvérbios 23:20-21',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2232021_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nProvérbios 23:20-21',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def apocalipse_2013():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Pelo que seremos julgado nos últimos dias?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Nossa fé",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22013_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Nosso arrependimento",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22013_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Nossas obras",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt12013_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Nossa liberdade",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22013_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt12013_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nApocalípse 20:13',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt22013_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nApocalípse 20:13',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def malaquias_456():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual a missão do profeta Elias \nantes da segunda vinda de Cristo",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Repreender os povos da terra",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2456_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Converter os descrentes",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2456_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Converter os pais aos filhos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1456_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Aliviar o espírito",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2456_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1456_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nMalaquias 4:5-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2456_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nMalaquias 4:5-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def proverbios_2813():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que acontece quando \nescondemos nossos pecados?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Ficamos com vergonha",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22813_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Sentimos tristeza",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22813_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Não teremos lembrança deles",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt22813_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Não prosperaremos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt12813_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt12813_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nProvérbios 28:13',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt22813_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nProvérbios 28:13',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def romanos_636():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual o simbolismo do batismo?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Nascimento e ressurreição",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2636_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Morte e nascimento",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2636_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Nascimento e morte",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2636_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Morte e ressurreição",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1636_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1636_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nRomanos 6:3-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2636_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nRomanos 6:3-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def Ipedro_11920():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Em que momento Cristo ficou sabendo \nque seria morto pelos nossos pecados?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Antes da fundação do mundo",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt111920_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Antes do seu ministério",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt211920_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Quando foi presso no Getsêmani",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt211920_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Durante a traição de Judas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt211920_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt111920_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nApocalipse 13:8',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt211920_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nApocalipse 13:8',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def tiago_156():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Como obter a sabedoria nesta vida?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Orar e compartilhar",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2156_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Jejuar com esperança",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2156_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Orar com fé",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1156_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Meditar sem duvidar",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2156_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1156_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nTiago 1:5-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2156_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nTiago 1:5-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def lucas_171119():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Quantos leprosos agradesseram \nao Senhor ao serem curados \nentre Samaria e Galiléia?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="3 leprosos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171119_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="5 leprosos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171119_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Nenhum leproso",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171119_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="1 leproso",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1171119_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1171119_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nLucas 17:11-19',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2171119_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nLucas 17:11-19',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def genesis_481314():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="De que forma José e Efraim \nforam abençoados por Jacó?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Pela imposição das mãos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1481314_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Pela fé e jejum",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2481314_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Pela oração coletiva",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2481314_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Pela fé em conjunto",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2481314_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1481314_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nGênesis 48:13-14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2481314_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nGênesis 48:13-14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def Ireis_171011():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="O que Elias pedio a viúva de Sarepta?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Água e pão",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1171011_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Um local para dormir",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171011_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Água e vinho",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171011_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Pão e mel",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171011_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1171011_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nI Reis 17:10-11',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2171011_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nI Reis 17:10-11',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def neemias_839():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="Qual a reação do povo ao \nouvir a leitura do livro \nda lei de Moisés?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Ouviu com atenção",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt1171011_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Ouviu e chorou",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171011_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Reclamou muito",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171011_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Não deu atenção",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt2171011_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt1839_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nNeemias 8:3,9',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt2839_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nNeemias 8:3,9',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------

# Método referente a pergunta

def amos_37():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text="A quem são revelados os segredos do Senhor?",
                     font='Verdana',
                     height=5,
                     bg='FireBrick',
                     fg='white').pack(fill=BOTH, expand=1)

    b1 = Button(filewin,
                text="Aos discípulos",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt237_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                text="Aos sacerdotes",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt237_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                text="Aos profetas",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt137_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                text="Ao povo de Israel",
                font='Verdana',
                height=2,
                bg='Khaki',
                command=bt237_onclick).pack(fill=BOTH, expand=1)


# Método referente a resposta

def bt137_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nAmós 3:7',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)


def bt237_onclick():
    filewin = Toplevel(janela)

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nAmós 3:7',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)


# -------------------------------------------------------------------------------------------------------


class Packing:
    def __init__(self, instancia):
        self.container0 = Frame(instancia)
        self.container1 = Frame(instancia)
        self.container2 = Frame(instancia)
        self.container3 = Frame(instancia)
        self.container4 = Frame(instancia)
        self.container5 = Frame(instancia)
        self.container6 = Frame(instancia)
        self.container7 = Frame(instancia)
        self.container8 = Frame(instancia)
        self.container9 = Frame(instancia)

        self.container0.pack(side=TOP)
        self.container1.pack(side=TOP)
        self.container2.pack(side=TOP)
        self.container3.pack(side=TOP)
        self.container4.pack(side=TOP)
        self.container5.pack(side=TOP)
        self.container6.pack(side=TOP)
        self.container7.pack(side=TOP)
        self.container8.pack(side=TOP)
        self.container9.pack(side=TOP)

        Button(self.container0, width=72, height=5, text='Você está pensando que conhece a Bíblia? \
Ou você sente que precisa conhecê-la melhor?\n Teste seus conhecimentos no jogo de perguntas \
e respostas sobre o Livro mais conhecido\n e respeitado de todos os tempos.',
               font=('Verdana', 15), bg='SteelBlue', fg='white').pack(side=TOP)

        Button(self.container1, width=18, height=3, text='Provérbios 28:13', font='Verdana', bg='FireBrick', fg='white',
               command=proverbios_2813).pack(side=RIGHT)
        Button(self.container1, width=18, height=3, text='Daniel 1:1-6', font='Verdana', bg='FireBrick', fg='white',
               command=daniel_116).pack(side=RIGHT)
        Button(self.container1, width=18, height=3, text='Provérbios 15:1', font='Verdana', bg='FireBrick', fg='white',
               command=proverbios_151).pack(side=RIGHT)
        Button(self.container1, width=18, height=3, text='Atos 18:2', font='Verdana', bg='FireBrick', fg='white',
               command=atos_182).pack(side=RIGHT)
        Button(self.container1, width=18, height=3, text='Gênesis 4:1-25', font='Verdana', bg='FireBrick', fg='white',
               command=geneses_4125).pack(side=RIGHT)
        Button(self.container2, width=18, height=3, text='Tiago 5:14', font='Verdana', bg='FireBrick', fg='white',
               command=tiago_514).pack(side=LEFT)
        Button(self.container2, width=18, height=3, text='Romanos 6:3-6', font='Verdana', bg='FireBrick', fg='white',
               command=romanos_636).pack(side=LEFT)
        Button(self.container2, width=18, height=3, text='João 1:48', font='Verdana', bg='FireBrick', fg='white',
               command=joao_148).pack(side=LEFT)
        Button(self.container2, width=18, height=3, text='Lucas 3:23', font='Verdana', bg='FireBrick', fg='white',
               command=lucas_323).pack(side=LEFT)
        Button(self.container2, width=18, height=3, text='Efésios 2:19-20', font='Verdana', bg='FireBrick', fg='white',
               command=efesios_21920).pack(side=LEFT)

        self.b4 = Button(self.container3, width=18, height=3, text='Mateus 4:3-4', font='Verdana', bg='FireBrick',
                         fg='white',
                         command=mateus_434)
        self.b41 = Button(self.container3, width=18, height=3, text='I Pedro 1:19-20', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=Ipedro_11920)
        self.b5 = Button(self.container3, width=18, height=3, text='Hebreus 11:1-3', font='Verdana', bg='FireBrick',
                         fg='white',
                         command=hebreus_1113)
        self.b6 = Button(self.container3, width=18, height=3, text='I Samuel 17:49-50', font='Verdana', bg='FireBrick',
                         fg='white',
                         command=Isamuel_174950)
        self.b7 = Button(self.container3, width=18, height=3, text='João 4:6-7', font='Verdana', bg='FireBrick',
                         fg='white',
                         command=joao_467)
        self.b8 = Button(self.container4, width=18, height=3, text='Êxodo 16:3', font='Verdana', bg='FireBrick',
                         fg='white',
                         command=exodo_163)
        self.b81 = Button(self.container4, width=18, height=3, text='Tiago 1:5-6', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=tiago_156)
        self.b9 = Button(self.container4, width=18, height=3, text='Isaias 1:18', font='Verdana', bg='FireBrick',
                         fg='white',
                         command=isaias_118)
        self.b10 = Button(self.container4, width=18, height=3, text='Marcos 10:46-52', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=marcos_104652)
        self.b11 = Button(self.container4, width=18, height=3, text='Mateus 4:18-19', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=mateus_41819)
        self.b12 = Button(self.container5, width=18, height=3, text='Josué 6:1-20', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=josue_6120)
        self.b121 = Button(self.container5, width=18, height=3, text='Lucas 17:11-19', font='Verdana', bg='FireBrick',
                           fg='white',
                           command=lucas_171119)
        self.b13 = Button(self.container5, width=18, height=3, text='João 12:12-13', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=joao_121213)
        self.b14 = Button(self.container5, width=18, height=3, text='I Coríntios 2:14', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=Icorintios_214)
        self.b15 = Button(self.container5, width=18, height=3, text='Lucas 19:45-48', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=lucas_194548)
        self.b16 = Button(self.container6, width=18, height=3, text='João 18:31', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=joao_1831)
        self.b161 = Button(self.container6, width=18, height=3, text='Gênesis 48:13-14', font='Verdana', bg='FireBrick',
                           fg='white',
                           command=genesis_481314)
        self.b17 = Button(self.container6, width=18, height=3, text='Mateus 26:63', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=mateus_2663)
        self.b18 = Button(self.container6, width=18, height=3, text='João 19:32', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=joao_1932)
        self.b19 = Button(self.container6, width=18, height=3, text='Atos 13:1-3', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=atos_1313)
        self.b20 = Button(self.container7, width=18, height=3, text='Mateus 27:30', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=mateus_2730)
        self.b201 = Button(self.container7, width=18, height=3, text='I Reis 17:10-11', font='Verdana', bg='FireBrick',
                           fg='white',
                           command=Ireis_171011)
        self.b21 = Button(self.container7, width=18, height=3, text='Gêneses 25:33', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=geneses_2533)
        self.b22 = Button(self.container7, width=18, height=3, text='Josué 24:32', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=josue_2432)
        self.b23 = Button(self.container7, width=18, height=3, text='Provérbios 23:20-21', font='Verdana',
                          bg='FireBrick', fg='white',
                          command=proverbios_232021)
        self.b24 = Button(self.container8, width=18, height=3, text='João 12:4-5', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=joao_1245)
        self.b241 = Button(self.container8, width=18, height=3, text='Neemias 8:3,9', font='Verdana', bg='FireBrick',
                           fg='white',
                           command=neemias_839)
        self.b25 = Button(self.container8, width=18, height=3, text='Apocalipse 14:6-7', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=apocalipse_27)
        self.b26 = Button(self.container8, width=18, height=3, text='Isaias 2:2-3', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=isaias_223)
        self.b27 = Button(self.container8, width=18, height=3, text='Apocalípse 20:13', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=apocalipse_2013)
        self.b28 = Button(self.container9, width=18, height=3, text='Malaquias 3:8-12', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=malaquias_3812)
        self.b281 = Button(self.container9, width=18, height=3, text='Amós 3:7', font='Verdana', bg='FireBrick',
                           fg='white',
                           command=amos_37)
        self.b29 = Button(self.container9, width=18, height=3, text='I Timóteo 4:1-3', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=Itimoteo_413)
        self.b30 = Button(self.container9, width=18, height=3, text='Joel 2:28-32', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=joel_22832)
        self.b31 = Button(self.container9, width=18, height=3, text='Malaquias 4:5-6', font='Verdana', bg='FireBrick',
                          fg='white',
                          command=malaquias_456)

        self.b4.pack(side=RIGHT, expand=1)
        self.b41.pack(side=RIGHT, expand=1)
        self.b5.pack(side=RIGHT, expand=1)
        self.b6.pack(side=RIGHT, expand=1)
        self.b7.pack(side=RIGHT, expand=1)
        self.b8.pack(side=RIGHT, expand=1)
        self.b81.pack(side=RIGHT, expand=1)
        self.b9.pack(side=RIGHT, expand=1)
        self.b10.pack(side=RIGHT, expand=1)
        self.b11.pack(side=RIGHT, expand=1)
        self.b12.pack(side=RIGHT, expand=1)
        self.b121.pack(side=RIGHT, expand=1)
        self.b13.pack(side=RIGHT, expand=1)
        self.b14.pack(side=RIGHT, expand=1)
        self.b15.pack(side=RIGHT, expand=1)
        self.b16.pack(side=RIGHT, expand=1)
        self.b161.pack(side=RIGHT, expand=1)
        self.b17.pack(side=RIGHT, expand=1)
        self.b18.pack(side=RIGHT, expand=1)
        self.b19.pack(side=RIGHT, expand=1)
        self.b20.pack(side=RIGHT, expand=1)
        self.b201.pack(side=RIGHT, expand=1)
        self.b21.pack(side=RIGHT, expand=1)
        self.b22.pack(side=RIGHT, expand=1)
        self.b23.pack(side=RIGHT, expand=1)
        self.b24.pack(side=RIGHT, expand=1)
        self.b241.pack(side=RIGHT, expand=1)
        self.b25.pack(side=RIGHT, expand=1)
        self.b26.pack(side=RIGHT, expand=1)
        self.b27.pack(side=RIGHT, expand=1)
        self.b28.pack(side=RIGHT, expand=1)
        self.b281.pack(side=RIGHT, expand=1)
        self.b29.pack(side=RIGHT, expand=1)
        self.b30.pack(side=RIGHT, expand=1)
        self.b31.pack(side=RIGHT, expand=1)


janela = Tk()
Packing(janela)
janela['bg'] = 'white'
janela.title('Conhecendo a Bíblia Sagrada')
janela.geometry('980x780+100+80')
menubar = Menu(janela)
janela.config(menu=menubar)


# ==============================================================
# Método Donothing
def donothing():
    filewin = Toplevel(janela)
    janela.geometry('980x780+100+70')
    lb0 = Label(filewin,
                text='==============================================================\nMomentos de Buscar Sabedoria e Refletir.\n==============================================================',
                bg='Black', fg='white', font='Verdana')
    lb01 = Label(filewin, text='', bg='Black')
    lb02 = Label(filewin, text='', bg='Black')
    lb03 = Label(filewin, text='', bg='Black')
    lb1 = Label(filewin, text='O Evangelho Está Funcionando para Você?', font=('times', 18, 'italic'), bg='white',
                width=80, height=2)
    lb2 = Label(filewin, text='Comece de Onde Está, Seja humilde sempre.', font=('times', 18, 'italic'), bg='yellow',
                width=80, height=2)
    lb3 = Label(filewin, text='Você É Digno de Ser Resgatado Pelo Senhor', font=('times', 18, 'italic'), bg='blue',
                fg='white', width=80, height=2)
    lb4 = Label(filewin, text='Precisamos Reservar Tempo Para Exercer A Fé.', font=('times', 18, 'italic'), bg='green',
                width=80, height=2)
    lb5 = Label(filewin, text='Não Deixe Que Nada Nem Ninguém O Impeça De Ser Vitorioso.', font=('times', 18, 'italic'),
                bg='DarkKhaki', width=80, height=2)
    lb6 = Label(filewin, text='A Oração Em Família Deve Ser Uma Prioridade Inadiável De Sua Vida Diária.',
                font=('times', 18, 'italic'), bg='Maroon', fg='white', width=80, height=2)
    lb7 = Label(filewin, text='“Rejeitar o mal e escolher o bem” (Isaías 7:15).', font=('times', 18, 'italic'),
                bg='Thistle', width=80, height=2)
    lb8 = Label(filewin, text='É importante erguer-nos acima das racionalizações e fazer as melhores escolhas.',
                font=('times', 18, 'italic'), bg='Lime', width=80, height=2)
    lb9 = Label(filewin, text='Quando racionalizamos as escolhas erradas, perdemos as bênçãos que necessitamos.',
                font=('times', 18, 'italic'), bg='SlateGray', width=80, height=2)
    lb10 = Label(filewin,
                 text='A imensidão do universo não mudou de repente, mas nossa \ncapacidade de ver e entender essa verdade mudou drasticamente.',
                 font=('times', 18, 'italic'), bg='SteelBlue', width=80, height=2)
    lb11 = Label(filewin,
                 text='Nosso conhecimento prévio pode até parecer tolice para nós porque o que \nantes era tão claro novamente se tornou borrado, embaçado e distante.',
                 fg='white', font=('times', 18, 'italic'), bg='Navy', width=80, height=2)
    lb12 = Label(filewin,
                 text='Acaso não temos motivo para encher-nos de gratidão, \nsejam quais forem as circunstâncias em que nos encontremos?',
                 font=('times', 18, 'italic'), bg='#00FFFF', width=80, height=2)
    lb13 = Label(filewin,
                 text='E aquele que receber todas as coisas com gratidão será glorificado; e as coisas desta Terra \nser-lhe-ão acrescentadas, mesmo centuplicadas, sim, mais',
                 font=('times', 18, 'italic'), bg='SkyBlue', width=80, height=2)

    lb0.pack(side=TOP, fill=X)
    lb01.pack(side=LEFT, fill=Y)
    lb02.pack(side=RIGHT, fill=Y)
    lb03.pack(side=BOTTOM, fill=X)
    lb1.pack(side=TOP, fill=BOTH, expand=1)
    lb2.pack(side=TOP, fill=BOTH, expand=1)
    lb3.pack(side=TOP, fill=BOTH, expand=1)
    lb4.pack(side=TOP, fill=BOTH, expand=1)
    lb5.pack(side=TOP, fill=BOTH, expand=1)
    lb6.pack(side=TOP, fill=BOTH, expand=1)
    lb7.pack(side=TOP, fill=BOTH, expand=1)
    lb8.pack(side=TOP, fill=BOTH, expand=1)
    lb9.pack(side=TOP, fill=BOTH, expand=1)
    lb10.pack(side=TOP, fill=BOTH, expand=1)
    lb11.pack(side=TOP, fill=BOTH, expand=1)
    lb12.pack(side=TOP, fill=BOTH, expand=1)
    lb13.pack(side=TOP, fill=BOTH, expand=1)


def exemplo1():
    filewin = Toplevel(janela)
    janela.geometry('980x780+100+80')
    lb0 = Label(filewin, text='\nMomento de Reflexão\n', bg='Black', fg='white')
    lb01 = Label(filewin, text='', bg='Black')
    lb02 = Label(filewin, text='', bg='Black')

    lb0.pack(side=TOP, fill=X)
    lb01.pack(side=LEFT, fill=Y)
    lb02.pack(side=RIGHT, fill=Y)

    T = Text(filewin, height=20, width=40, bg='LightYellow', font=('times', 20, 'italic'))
    T.pack()

    T.insert(END, "    Gratos em Quaisquer Circunstâncias \n\n    É fácil ser grato \
por coisas quando a vida parece estar a nosso favor. Mas, e naqueles momentos \
em que as coisas que desejamos parecem estar muito fora de nosso alcance? Em \
outras palavras, estou sugerindo que, em vez de sermos “gratos por coisas”, \
devemos concentrar-nos em ser “gratos em nossas circunstâncias” — sejam elas \
quais forem. Se formos gratos a Deus em nossas circunstâncias, podemos vivenciar \
uma doce paz, em meio à tribulação. Mesmo na aflição, podemos elevar nosso coração \
em louvor. Na dor, podemos gloriar-nos na Expiação de Cristo. No frio da amarga \
tristeza, podemos sentir a proximidade e o calor do abraço do céu. \n    A verdadeira \
gratidão é uma expressão de esperança e testemunho. Advém do reconhecimento de que \
nem sempre compreendemos as provações da vida, mas confiamos que um dia compreenderemos. \
Quanto mais aprendemos sobre o evangelho de Jesus Cristo, mais nos damos conta de \
que os finais aqui da mortalidade não são finais, de modo algum. São meras interrupções \
— pausas temporárias que um dia parecerão pequenas, em comparação com a alegria eterna \
reservada para os fiéis. \n    Irmãos e irmãs, acaso não temos motivo para encher-nos de \
gratidão, sejam quais forem as circunstâncias em que nos encontremos? Acaso precisamos \
de maior motivo para ter nosso coração “cheio de agradecimento a Deus”? “Não temos, \
portanto, motivo para regozijar-nos?” Seremos imensamente abençoados se reconhecermos a \
obra da mão de Deus no maravilhoso tapete da vida! \n    A gratidão a nosso Pai Celestial \
amplia nossa percepção e clareia nossa visão. A gratidão é um grande catalisador de \
todos os atributos cristãos! Um coração grato é a fonte de todas as virtudes. O Senhor \
prometeu: “E aquele que receber todas as coisas com gratidão será glorificado; e as \
coisas desta Terra ser-lhe-ão acrescentadas, mesmo centuplicadas, sim, mais”. Ergamos \
sempre e constantemente a voz e demonstremos por palavras e atos a nossa gratidão a \
nosso Pai Celestial e a Seu Amado Filho, Jesus Cristo.")


# ==============================================================
# Menu Arquivo
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=filemenu)

# Submenu de Arquivo
filemenu.add_command(label="Palavras de Sabedoria", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Momentos de Reflexões", command=exemplo1)

# ==============================================================


janela.mainloop()
