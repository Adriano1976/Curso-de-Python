import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
home = 'https://pt.stackwverflow.com'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

print()
for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(f'Home: {home}\n'
          f'Link: {titulo["href"]}\n')
