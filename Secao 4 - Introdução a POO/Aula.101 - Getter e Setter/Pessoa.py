class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        # Isso é leitura
        return self.nome + ' ' + self.sobrenome

    @nome_completo.setter
    def nome_completo(self, nome_completo):
        # Isso é escrita
        nome_quebrado_em_espacos = nome_completo.split(' ')

        if len(nome_quebrado_em_espacos) < 2:
            raise ValueError('Envie nome e sobrenome')

        self.nome = nome_quebrado_em_espacos[0]
        self.sobrenome = ' '.join(nome_quebrado_em_espacos[1:])


if __name__ == "__main__":
    pessoa = Pessoa('Luiz', 'Otávio')
    print(pessoa.nome_completo)  # Luiz Otávio

    pessoa.nome_completo = 'João Silva'
    print(pessoa.nome)  # João
    print(pessoa.sobrenome)  # Silva
    print(pessoa.nome_completo)  # João Silva
