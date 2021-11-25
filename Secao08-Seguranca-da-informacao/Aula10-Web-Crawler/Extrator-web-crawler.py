"""
- A ferramenta "Web crawler" é usada para encontrar, ler e indexar páginas de um site. É como um robô que
captura informações de cada um dos links que encontra pela frente, cadastra e compreende o que é mais relevante.
(palavras - chaves)
- Muito utilizado em levantamento de informações em um processo de pentest.
- A biblioteca "BeautifulSoup" serve para extrair dados de arquivos HTML e XML.
- A biblioteca "operator" serve para exportar um conjunto de funções eficientes correspondentes aos operadores
intrínsecos do Python como: +-*/not and.
- A biblioteca "collections" serve para ajudar a preencher e manipular eficientemente as estruturas de dados
como tuplas, dicionários e listas.
"""

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):
    wordlist = []
    source_code = requests.get(url).text

    # Esse objeto irá fazer a requisição dos dados do html e transforma-los em texto.
    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


# Essa função serve para limpar todos os símbolos da lista extraida do html, deixando somente palavras.
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|/;:<>"?.,'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


# Essa função serve para criar um dicionário com a lista de palavras criada anteriormente e conta-las.
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(f'{key, value}')

    c = Counter(word_count)

    top = c.most_common(10)
    print(f'\nTop 10: {top}')


if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
