import requests
from bs4 import BeautifulSoup


class Cor:
    ROXO = '\033[95m'
    CIANO = '\033[96m'
    CIANOESCURO = '\033[36m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'

    NEGRITO = '\033[1m'
    UNDERLINE = '\033[4m'

    TERMINA = '\033[0m'


url = 'https://pt.stackoverflow.com/questions/tagged/python'
home = 'https://pt.stackwverflow.com'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

print()
for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(f'{Cor.CIANOESCURO}Home:{Cor.TERMINA} {home}\n'
          f'{Cor.VERMELHO}Link:{Cor.TERMINA} {titulo["href"]}\n')
