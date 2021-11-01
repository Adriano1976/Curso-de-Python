from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    data_atual = datetime.strftime(datetime.now(), '%d-%m-%Y')
    hora_atual = datetime.strftime(datetime.now(), '%H:%M:%S')

    def __init__(self, nome, idade, dormindo=False, comendo=False, bebendo=False, falando=False, dirigindo=False):
        self.nome = nome
        self.idade = idade
        self.dormindo = dormindo
        self.comendo = comendo
        self.bebendo = bebendo
        self.falando = falando
        self.dirigindo = dirigindo

    def comer(self, alimento):
        if self.comendo:
            return f'{self.nome} já está comendo.'
        if self.falando:
            return f'{self.nome} não pode comer enquanto está falando.'
        if self.bebendo:
            return f'{self.nome} não pode comer enquanto está bebendo'
        if self.dormindo:
            return f'{self.nome} não pode comer enquanto está dormindo.'
        if self.dirigindo:
            return f'{self.nome} não pode comer enquanto está dirigindo.'
        self.comendo = True
        return f'{self.nome} está comendo {alimento}.'

    def parar_comer(self):
        if not self.comendo:
            return f'{self.nome} não está comendo.'
        self.comendo = False
        return f'{self.nome} parou de comer.'

    def beber(self, liquido):
        if self.bebendo:
            return f'{self.nome} já está bebendo.'
        if self.comendo:
            return f'{self.nome} não pode comer enquanto está bebendo.'
        if self.falando:
            return f'{self.nome} não pode beber enquanto está falando.'
        if self.dormindo:
            return f'{self.nome} não pode beber enquanto está dormindo.'
        if self.dirigindo:
            return f'{self.nome} não pode beber enquanto está dirigindo.'
        self.bebendo = True
        return f'{self.nome} está bebendo {liquido}.'

    def parar_beber(self):
        if not self.bebendo:
            return f'{self.nome} não está bebendo.'
        self.bebendo = False
        return f'{self.nome} parou de beber.'

    def falar(self, assunto):
        if self.falando:
            return f'{self.nome} já está falando.'
        if self.comendo:
            return f'{self.nome} não pode falar enquanto está comendo.'
        if self.bebendo:
            return f'{self.nome} não pode falar enquanto está bebendo'
        if self.dormindo:
            return f'{self.nome} não pode falar enquanto está dormindo.'
        if self.dirigindo:
            return f'{self.nome} não pode falar enquanto está dirigindo.'
        self.falando = True
        return f'{self.nome} está falando sobre {assunto}.'

    def parar_falar(self):
        if not self.falando:
            return f'{self.nome} não está falando.'
        self.falando = False
        return f'{self.nome} parou de falar.'

    def dormir(self):
        if self.dormindo:
            return f'{self.nome} já está dormindo.'
        if self.comendo:
            return f'{self.nome} não pode dormir enquanto está comendo.'
        if self.bebendo:
            return f'{self.nome} não pode dormir enquanto está bebendo'
        if self.falando:
            return f'{self.nome} não pode dormir enquanto está falando'
        if self.dirigindo:
            return f'{self.nome} não pode dormir enquanto está dirigindo.'
        self.dormindo = True
        return f'{self.nome} está dormindo.'

    def parar_dormir(self):
        if not self.dormindo:
            return f'{self.nome} não está dormindo.'
        self.dormindo = False
        return f'{self.nome} parou de dormir.'

    def dirigir(self, transporte):
        if self.dirigindo:
            return f'{self.nome} já está dirigindo.'
        if self.falando:
            return f'{self.nome} não pode dirigir enquanto está falando.'
        if self.bebendo:
            return f'{self.nome} não pode dirigir enquanto está bebendo.'
        if self.dormindo:
            return f'{self.nome} não pode dirigir enquanto está dormindo.'
        if self.comendo:
            return f'{self.nome} não pode dirigir enquanto está comendo.'
        self.dirigindo = True
        return f'{self.nome} está dirigindo {transporte}.'

    def parar_dirigir(self):
        if not self.dirigindo:
            return f'{self.nome} não está dirigindo.'
        self.dirigindo = False
        return f'{self.nome} parou de digirir.'

    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        return ano_nascimento

    def get_atual_ano(self):
        ano_atual = self.ano_atual
        return f'{self.nome} está vivendo no ano de {ano_atual}.'

    def get_data_atual(self):
        data = self.data_atual
        return f'{self.nome} informa que a data atual é {data}.'

    def get_hora_atual(self):
        hora_atual = self.hora_atual
        return f'{self.nome} informa que o horário atual são {hora_atual}.'

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
