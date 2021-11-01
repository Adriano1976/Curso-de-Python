"""
- Teste realizado no Windows - ping 127.0.0.1
- subprocess ajuda no monitoramento de servidores por meio de comandos para veriguação de dados
de saída.
- De forma resumida e direta, "subprocess" serve para executar comandos no sistema operacional.
- https://docs.python.org/pt-br/3/library/subprocess.html
"""
import subprocess

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True,
    encoding='cp850'
)

saida = proc.stdout
print(saida)
