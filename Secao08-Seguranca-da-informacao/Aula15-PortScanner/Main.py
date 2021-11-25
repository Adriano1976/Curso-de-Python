"""
- Estava ocorrendo o seguinte erro:
- nmap.PortScannerError: 'nmap program was not found in path. PATH is : C:\\W
- INDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\Python27;D:\\WPS Of
- fice\\9.1.0.4468\\office6;C:\\Program Files\\Microsoft Visual Studio\\Common\\To
- ols\\WinNT;C:\\Program Files\\Microsoft Visual Studio\\Common\\MSDev98\\Bin;C:\\
- Program Files\\Microsoft Visual Studio\\Common\\Tools;C:\\Program Files\\Microso
- ft Visual Studio\\VC98\\bin'

 por isso instalei o nmap localmente na máquina.
- link de download:https://nmap.org/download.html

- depois de instalado defini o endereço local no nmap_path, para que fosse reconhecido na execução do código.
"""

import nmap

nmap_path = ('nmap', '/usr/bin/nmap', '/usr/local/bin/nmap', '/sw/bin/nmap',
             '/opt/local/bin/nmap'r"C:\Program Files (x86)\Nmap\nmap.exe")
scanner = nmap.PortScanner(nmap_search_path=nmap_path)
nomeUsuario = input("Informe seu nome: ")
print("Olá, {}! Bem-vindo ao PythonSCANNER!".format(nomeUsuario))
print("<------------------------------------------------------------>")

ip = input("Qual o endereço de IP você deseja escanear? ")
print("Verificando o endereço: ", ip)
type(ip)

menu = input("""\n Escolha qual a varredura a ser efetuada
                1 -> Varredura SYN
                2 -> Varredura UDP
                3 -> Varredura Intensa
                Digite a opção desejada: """)
print("A Opção de varredura escolhida foi: ", menu)

if menu == "1":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("As Portas abertas e disponíveis no ip informado são: ", scanner[ip]['tcp'].keys())

elif menu == "2":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("As Portas abertas e dispníveis no ip informado são: ", scanner[ip]['udp'].keys())

elif menu == "3":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("As Portas abertas e disponíveis no ip informado são: ", scanner[ip]['tcp'].keys())
else:
    print("Escolha uma das opções do menu: ")
