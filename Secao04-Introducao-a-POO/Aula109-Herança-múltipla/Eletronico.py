from Log import LogMixin
from Archive import Archive


class Eletronico(LogMixin, Archive):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False  # Desligado

    def ligar(self):
        if self._ligado:
            error: str = f'{self._nome} JÁ ESTÁ LIGADO.'
            print(error)
            self.log_error(error)
            self.text_error(error)
            return

        info: str = f'{self._nome} ESTÁ LIGADO.'
        print(info)
        self.log_info(info)
        self.text_info(info)
        self._ligado = True  # Ligado

    def desligar(self):
        if not self._ligado:
            error: str = f'{self._nome} JÁ ESTÁ DESLIGADO.'
            print(error)
            self.log_error(error)
            self.text_error(error)
            return

        info: str = f'{self._nome} ESTÁ DESLIGADO.'
        print(info)
        self.log_info(info)
        self.text_info(info)
        self._ligado = False  # Desligado
