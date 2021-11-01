# Módulos padrão do Curso-de-Python:
# Módutos são arquivos .py (que contém código python) e servem para expandir as funcionalidades padrão da linguagem.

import sys
from random import randint

print(f'Sistema Operacional: {sys.platform}')

for var in range(10):
    print(randint(0, 10))
