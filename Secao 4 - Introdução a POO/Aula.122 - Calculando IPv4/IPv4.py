import re


def ipv4(ip, mascara=None, prefixo=None):
    global rede, num_ips, broadcast

    def to_bin(ip):
        ip_lista = ip.split('.')
        bin_lista = [(bin(int(x)))[2:].zfill(8) for x in ip_lista]
        ip_bin = ''.join(bin_lista)

        return ip_bin

    def to_dec(bin):
        n = 8
        ip_lista = [str(int(bin[i:i + n], 2)) for i in range(0, len(bin), 8)]
        ip_dec = '.'.join(ip_lista)

        return ip_dec

    regexp = re.compile(r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')

    if regexp.search(ip):

        if not prefixo:  # Find the prefix if not given.
            prefixo = to_bin(mascara).count('1')

        if not mascara:  # Find the mask, if not given.
            mascara_bin = (prefixo * '1').ljust(32, '0')
            mascara = to_dec(mascara_bin)

        host_bits = 32 - int(prefixo)  # Find the number of hosts.

        rede_bin = to_bin(ip)[:prefixo] + (host_bits * '0')  # Find the network.
        rede = to_dec(rede_bin)

        broadcast_bin = to_bin(ip)[:prefixo] + (host_bits * '1')  # Find the broadcast.
        broadcast = to_dec(broadcast_bin)

        num_ips = 2 ** host_bits - 2

    print(f'\nO IP é {ip}\nA máscara é {mascara}\nA rede é {rede}\n'
          f'O broadcast é {broadcast}\nOs números de ips são {num_ips}')
