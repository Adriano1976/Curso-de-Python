"""
- Documentação: https://pythonhosted.org/PyPDF2/
- Mais exemplos de uso: http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
- pip install pypdf2 # virtualenv
- pipenv install pypdf2 # pipenv
"""

import PyPDF2

caminho_dos_pdfs = r'doc_pdf/'

with open(r'doc_pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_paginas in range(num_paginas):
        escrito = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_paginas)
        escrito.addPage(pagina_atual)

        with open(f'novos_doc_pdf/{num_paginas}.pdf', 'wb') as novo_pdf:
            escrito.write(novo_pdf)
