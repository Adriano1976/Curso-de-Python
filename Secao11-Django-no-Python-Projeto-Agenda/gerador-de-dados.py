"""
- Esse é um script pra gerar 210 contatos, coloca ele gerado num arquivo em .sql e
abre o DB browser e bota pra executar.
- Obs.: Data pode também sair formatada - datetime.now().strftime('%d/%m/%Y %H:%M:%S')

"""

from random import *
from datetime import datetime

nomes = 'Miguel Arthur Heitor Bernardo Théo Davi Gabriel Pedro Samuel Lorenzo Benjamin Matheus ' \
        'Lucas Benício Gael Joaquim Nicolas Henrique Rafael Isaac Guilherme Murilo Lucca Gustavo ' \
        'João Miguel Noah Felipe Anthony Enzo João Pedro Pietro Bryan Daniel Pedro Henrique Enzo ' \
        'Gabriel Leonardo Vicente Valentim Eduardo Antônio  Emanuel Davi Lucca João João Lucas Adriano'

nomes = nomes.split()

sobrenomes = 'Abbott Abernathy Adair Adams Adkins Aguirre Alexander Allen Allison Almeida Alvarado ' \
             'Alvarez Andersen Anderson Anderson Andrews Archer Armstrong Arnold Arsenault Ashby ' \
             'Ashworth Atkinson Austin Ayers Fagan Fallon Fanning Farley Farrell Faulkner Ferguson ' \
             'Fernandez Figueroa Finch Finn Finnegan Fischer Fisher Fitch Fitzgerald Fitzpatrick ' \
             'Fitzsimmons Flanagan Fletcher Flood Flores Floyd Flynn Forbes Ford Forsyth Foster ' \
             'Fournier Fowler Fox Franklin Fraser Frazier Freeman Frost Fry Fuller Smith'

sobrenomes = sobrenomes.split()
for i in range(1, 210):
    nome = choice(nomes)
    sobrenome = choice(sobrenomes)
    email = nome + '@gmail.com'
    data_criacao = datetime.now()
    descricao = 'Gerado a partir de um script.'
    categoria_id = randint(1, 4)  # Supondo que você tem 3 categorias, caso não, só alterar o segundo valor.
    telefone = str(randint(888888888, 999999999))

    print(f"INSERT INTO contatos_contato"
          f" (nome, sobrenome, email, data_criacao, descricao, categoria_id, telefone)"
          f" VALUES ('{nome}', '{sobrenome}', '{email}', '{data_criacao}', '{descricao}', '{categoria_id}', '{telefone}');")
