import re


class CalcIPv4:

    def __init__(self, ip=None, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def prefixo(self):
        return self._prefixo

    @property
    def numeroIPs(self):
        return self._get_numero_ips()

    @ip.setter
    def ip(self, value):
        if not self._valide(value):  # Informing an exception if the value of the IP number is wrong.
            raise ValueError('IP inválido.')

        self._ip = value
        self._ip_bin = self._ip_to_bin(value)

    @mascara.setter
    def mascara(self, value):
        if not value:
            return

        if not self._valide(value):  # Informing an exception if the value of the "mask" number is wrong.
            raise ValueError('Máscara inválida.')

        self._mascara = value
        self._mascara_bin = self._ip_to_bin(value)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, value):
        if not value:
            return

        if not isinstance(value, int):  # Informing an exception if the "prefix" value is not an integer.
            raise TypeError('Prefixo precisa ser inteiro.')

        if value > 32:  # Informing an exception if the "prefix" value is greater than 32 bits.
            raise TypeError('Prefixo precisa ter 32Bits.')

        self._prefixo = value
        self._mascara_bin = (value * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valide(value):  # Validating IP numbers, masks and prefixes.
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(value):  # If the value is correct, it returns a true value.
            return True

    @staticmethod
    def _ip_to_bin(ip):  # Converting ip to binary.
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_binarios)  # Returns the value already converted to binary.

    @staticmethod
    def _bin_to_ip(ip):  # Convert binary numbers to ip.
        number = 8
        blocos = [str(int(ip[i:number + i], 2)) for i in range(0, 32, number)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):  # Check network ip number.
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._broadcast

    def _get_numero_ips(self):  # Check the amount of available ips on the network.
        return (2 ** (32 - self.prefixo)) - 2
