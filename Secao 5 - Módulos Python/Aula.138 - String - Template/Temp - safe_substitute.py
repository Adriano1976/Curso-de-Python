"""
- Ao usar 'safe_substitute', ele não vai ligar pra quantidade de Ply usados em html, evitando dar erro
na execursão do programa.
- Sempre coisas que vc tem certeza que não podem "machucar" o sistema, pode usar sem safe...
Se vc for receber dados do usuário, nesse caso tem que pensar bem antes de permitir qualquer coisa,
então usa safe.
"""

from string import Template
from datetime import datetime

with open('Template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')  # Informando data atual
    corpo_msg = template.safe_substitute(nome='Adriano Santos', data=data_atual)

    print(corpo_msg)
