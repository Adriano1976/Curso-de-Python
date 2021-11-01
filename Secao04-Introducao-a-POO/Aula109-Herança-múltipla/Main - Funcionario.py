from Funcionario import Gerente, Diretor, Supervisor, Vendedor, SistemaInterno

if __name__ == '__main__':
    diretor = Diretor('Adriano Santos', '254.256.458-45', 5000.0)
    gerente = Gerente('José Maria', '105.254.166-45', 4000.0)
    supervisor = Supervisor('Neide Ferreira', '267.005.457-68', 3000.0 )
    vendedor = Vendedor('Laura Beatriz', '456.458.005.85', 1000.0)

    sistema = SistemaInterno()
    sistema.login(diretor)
    sistema.login(gerente)
    sistema.login(supervisor)
    sistema.login(vendedor)

    print(f'\nDiretor: {diretor.nome}')
    print(f'Salário: {diretor.salario}')
    print(f'Bonificação: {diretor.get_bonificacao()}')

    print(f'\nGerente: {gerente.nome}')
    print(f'Salário: {gerente.salario}')
    print(f'Bonificação: {gerente.get_bonificacao()}')

    print(f'\nSupervisor: {supervisor.nome}')
    print(f'Salário: {supervisor.salario}')
    print(f'Bonificação: {supervisor.get_bonificacao()}')

    print(f'\nVendedor: {vendedor.nome}')
    print(f'Salário: {vendedor.salario}')
    print(f'Bonificação: {vendedor.get_bonificacao()}')

