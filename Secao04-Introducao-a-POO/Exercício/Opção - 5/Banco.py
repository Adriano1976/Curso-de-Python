class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        if cliente.conta.agencia not in self.agencias:
            print(f'Não incluiu a conta do cliente {cliente.nome} porque a Agência é inválida!')
            print('=' * 70)
            return
        # Agregando as classes cliente e conta
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)
        print(f'{cliente.nome} incluido no banco na Ag: {cliente.conta.agencia} e C/C: {cliente.conta.conta}')
        print('=' * 70)

    # def inserir_conta(self, conta):
    #     self.contas.append(conta)

    def autenticar(self, cliente):
        print(f'Autenticando {cliente.nome}...')
        if cliente not in self.clientes:  # Verifica se o objeto inteiro cliente está em clientes
            print('Cliente não tem conta no banco!')
            return False
        # Como só incluo o cliente/conta se a agência for válida, não preciso fazer os testes abaixo:
        # if cliente.conta not in self.contas:  # Verifica se o objeto inteiro conta do cliente está em contas
        #     print(f'Conta {cliente.conta}...')
        #     return False
        # if cliente.conta.agencia not in self.agencias:  # verifica se a agência está em agências
        #     print(f'Agencia {cliente.conta.agencia}...')
        #     return False
        print(f'{cliente.nome} autenticado!')
        return True
