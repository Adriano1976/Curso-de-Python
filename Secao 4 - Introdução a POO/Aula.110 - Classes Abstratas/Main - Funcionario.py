from Funcionario import Gerente, Diretor

if __name__ == '__main__':
    diretor = Diretor('Adriano Santos', '254.256.458-45', 5000.0)
    gerente = Gerente('José Maria', '105.254.166-45', 5000.0)

    print(f'\nDiretor: {diretor.nome}')
    print(f'Salário: {diretor.salario}')
    print(f'Bonificação: {diretor.get_bonificacao()}')

    print(f'\nGerente: {gerente.nome}')
    print(f'Salário: {gerente.salario}')
    print(f'Bonificação: {gerente.get_bonificacao()}')
