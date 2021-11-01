from Eletronico import Eletronico
from Log import LogMixin
from Archive import Archive


class Smartphone(Eletronico, LogMixin, Archive):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info: str = f'{self._nome} ESTÁ LIGADO.'
            print(info)
            self.log_error(info)
            self.text_error(info)
            return

        if self._conectado:
            error: str = f'{self._nome} JÁ ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            self.text_error(error)
            return

        info: str = f'{self._nome} ESTÁ CONECTADO.'
        print(info)
        self.log_info(info)
        self.text_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            info: str = f'{self._nome} ESTÁ DESLIGADO.'
            print(info)
            self.log_error(info)
            self.text_error(info)
            return

        if not self._conectado:
            error: str = f'{self._nome} JÁ ESTÁ DESCONECTADO.'
            print(error)
            self.log_error(error)
            self.text_error(error)
            return

        info: str = f'{self._nome} ESTÁ DESCONECTADO.'
        print(info)
        self.log_info(info)
        self.text_info(info)
        self._conectado = False
