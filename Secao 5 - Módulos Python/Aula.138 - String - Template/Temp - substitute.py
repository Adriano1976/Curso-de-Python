"""
- Ao usar 'substitute', ele vai ligar pra quantidade de Ply usados em html dando erro
na execursão do programa.
"""

from string import Template
from datetime import datetime

with open('Template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Adriano Santos', data=data_atual)

print(corpo_msg)
