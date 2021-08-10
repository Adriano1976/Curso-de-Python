"""
- Ao usar 'safe_substitute', ele não vai ligar pra quantidade de Ply usados em html, evitando dar erro
na execursão do programa.
"""

from string import Template
from datetime import datetime

with open('Template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')  # Informando data atual
    corpo_msg = template.safe_substitute(nome='Adriano Santos', data=data_atual)

    print(corpo_msg)
