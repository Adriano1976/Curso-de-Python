"""
- A ferramenta "web scraper" serve para coleta de dados web. É uma forma de mineração que permite a
extração de dados de sites da web convertendo-os em informação estruturada para posterior análise.
- A Biblioteca "BeautifulSoup" serve para extrair dados de arquivos HTML e XML.
- A Biblioteca "requests" permite que você envie solicitações HTTP em Python.
"""

from bs4 import BeautifulSoup
import requests


# O objeto seite recebe o conteudo da requisição htpp do site...
site = requests.get('https://www.climatempo.com.br/').content

# O objeto soup baixa do site o html
soup = BeautifulSoup(site, 'html.parser')

# O prettify transforma o html em string e o print vai exibir o html.
print(soup.prettify())

print('-' * 130)

# Extraindo informações expecíficas e exibindo o resultado da extração.
temperatura = soup.find(class_="-gray _flex _align-center")

print(f'\nInformações Extraidas Sobre Temperaturas:\n\n {temperatura}')
print(f'\nTítulo do Site: {soup.title.string}')
