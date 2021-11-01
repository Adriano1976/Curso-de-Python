inicio = True
logged = []
password = []
nome = []
idade = []
cpf = []
lista = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç', 'Z', 'X',
         'C', 'V', 'B', 'N', 'M']
lista_2 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', 'z', 'x',
           'c', 'v', 'b', 'n', 'm']
invalidos = ['123456', '78912', '567891', '234567', '345678', '456789', '567891', '678912', '789123', '891234',
             '912345']
cont = 1
while inicio:
    print('----Sistema de cadastro de clientes----')
    print('1- Cadastrar usuário')
    print('2- Deletar usuário')
    print('3- login')
    print('4- Sair')
    tela_inicial = input('Digite uma opção: ')
    if not tela_inicial.isnumeric() or tela_inicial <= '0' or tela_inicial > '4':
        erro_1 = True
        while erro_1:
            tela_inicial = input('Erro! Digite um número inteiro positivo, menor ou igual a 4 ou maior que 0: ')
            erro_1 = False if tela_inicial.isnumeric() and tela_inicial > '0' and tela_inicial <= '4' else True

    tela_inicial = int(tela_inicial)
    if tela_inicial == 1:
        cadastro = True
        while cadastro:
            ex = 0
            cadast_usuario = input(
                'Digite um login com 10/6 caracteres ou números para cadastro ou digite s para voltar: ')
            if cadast_usuario == 's':
                break
            elif cadast_usuario != 's' and cadast_usuario in logged:
                erro_1 = True
                while erro_1:
                    cadast_usuario = input(
                        'Esse nome de usuário já existe no sistema, favor digite um nome diferente ou digite s para voltar: ')
                    erro_1 = False if cadast_usuario not in logged or cadast_usuario == 's' else True


            def error_2(senha_1, senha_2, list, numeros, usuario,
                        list2):  # função criada para checar a senha eo login do usuário
                y = 1 if senha_1 in numeros else 0
                x = 1
                b = 1
                z = 1
                c = 0
                c2 = 0
                c1 = 0
                for valor in usuario:
                    if not valor.isnumeric() and valor in list2:  # aqui checou se o login do usuário possui letras
                        b = 0
                        c += 1  # aqui o contador conta a quantidade de letras que o login possui possui(ele deve conter 4 letras minúsculas)
                    elif valor.isnumeric():  # aqui checou se o login possui números
                        c2 += 1  # aqui o contador conta a quantidade de números que o login possui(ele deve conter 2 números)
                for valor in senha_1:
                    if not valor.isnumeric() and valor in list:  # aqui checou se a senha contém pelo menos uma letra máiuscula
                        x = 0
                    elif not valor.isnumeric() and valor in list2:  # aqui vai checar se a senha contém pelo menos uma letra minúscula
                        c1 = 0
                    elif valor.isnumeric():  # aqui checou se a senha contém pelo menos 1 número
                        z = 0
                if y == 0 and x == 0 and z == 0 and b == 0 and c == 4 and c1 == 0 and c2 == 2 and len(
                        senha_1) == 6 and senha_1 == senha_2:
                    return False
                else:
                    return True


            cadast_senha = input('Digite uma senha de 6 caracteres com pelo menos 1 letra máiscula e números: ')
            cadast_senha2 = input('Confirme a senha: ')
            cadast_usuario = ''.join(cadast_usuario.split())
            cadast_senha = ''.join(cadast_senha.split())
            erro_1 = error_2(cadast_senha, cadast_senha2, lista, invalidos, cadast_usuario, lista_2)
            while erro_1:
                ex = 1
                print('Erro! digite uma senha válida ou nome de usuário válido!')
                erro_1 = False
            if erro_1 == False and ex == 0 and len(cadast_usuario) <= 10 and len(cadast_usuario) >= 6:
                logged.append(cadast_usuario)
                password.append(cadast_senha)
                print('Usuário cadastrado com sucesso!')
                cadastro = False


    elif tela_inicial == 2:
        excluir = True
        while excluir:
            delete_usuario = input('Digite o login do usuário para o excluir do sistema ou digite s para voltar: ')
            delete_senha = input('Digite a senha do usuário ou digite s para voltar: ')
            if delete_usuario == 's' or delete_senha == 's':
                break
            if delete_usuario in logged and delete_senha in password:
                for indice, usuario in enumerate(logged):
                    if usuario == delete_usuario and password[indice] == delete_senha:
                        del (logged[indice])
                        del (password[indice])
                        print('Usuário excluido com sucesso do sistema!')
                        excluir = False
                    elif usuario == delete_usuario and password[indice] != delete_senha:
                        print('Erro! Senha incopátivel com usuário!')
            elif delete_usuario not in logged or delete_senha not in password:
                print('Usuário não encontrado no sistema, favor digite um usuário existente!')
                deletar = True
                while deletar:
                    delete = input('Digite 1 para deletar outro usuário ou digite 2 para sair: ')
                    if not delete.isnumeric() or delete <= '0' or delete > '2':
                        print('Erro! Digite apenas 1 ou 2 como opção!')
                    elif delete.isnumeric() and delete > '0' and delete <= '2':
                        if delete == '1':
                            deletar = False
                        else:
                            deletar = False
                            excluir = False

    elif tela_inicial == 3:
        logou = False
        log = True
        logado = False
        while log:
            login = input('Digite o login do usuário ou digite enter para voltar: ')
            senha = input('Digite a senha do usuário ou digite enter para voltar: ')
            if login == '' or senha == '':
                log = False
            else:
                if login in logged and senha in password:
                    for indice, valor in enumerate(logged):
                        if valor == login and password[indice] == senha:
                            logado = True
                            continue
                        elif valor == login and password[indice] != senha:
                            print('Erro! senha, inválida favor digitar novamente o login e a senha correta!')
                            log = False
                else:
                    erro_1 = True
                    while erro_1:
                        retorno = input(
                            'Erro! login e senha não encontrados no sistema, digite 1 para digitar o login e senha novamente ou 2 para voltar ao menu principal: ')
                        if not retorno.isnumeric() or retorno <= '0' or retorno > '2':
                            print('Erro! Opção inválida digite 1 ou 2!')
                        elif retorno.isnumeric() and retorno > '0' and retorno <= '2':
                            erro_1 = False if retorno == '1' or retorno == '2' else True
                            log = False if retorno == '2' and logou == False else True

            while logado:
                print('----Menu-Principal----')
                print('1- Cadastrar cliente')
                print('2- Lista de clientes cadastrados')
                print('3- Pesquisar cliente')
                print('4 Excluir cliente')
                print('5- Deslogar do sistema')
                tela_log = input('Digite uma opção: ')
                erro_1 = True if not tela_log.isnumeric() or tela_log <= '0' or tela_log > '5' else False
                while erro_1:
                    print('Erro, Digite um número menor ou igual a 5 ou maior que 0!')
                    erro_1 = False
                if tela_log == '1':
                    def error_1(list, nome_c):  # função criada para retornar o valor verdadeiro ou falso
                        x = 0
                        for valor in nome_c:
                            x += 1
                            if valor not in list or len(
                                    nome_c) < 6:  # caso o valor não esteja em list ou a quantidade de letras for menor que 6 retorna-rá um valor de erro True
                                return True
                            elif x == len(nome_c):
                                return False


                    opcao = True
                    while opcao:
                        ex = 0
                        nome_cliente = input(
                            'Digite o nome do cliente com letras máiusculas ou aperte enter para voltar: ')
                        save_nome = nome_cliente  # aqui foi criado a váriavel sava_nome para salvar o nome do cliente antes de unir com os espaços
                        nome_cliente = ''.join(
                            nome_cliente.split())  # aqui se uniu o nome do cliente para checar se o nome contém menos de 6 caracteres
                        if erro_1 == False and nome_cliente == '':
                            break
                        erro_1 = error_1(lista,
                                         nome_cliente)  # aqui a váriavel erro_1 receberá o valor que será retornado da função error

                        while erro_1:
                            ex = 1
                            print(
                                'Erro! Digite um nome válido com mais de 6 caracteres com letras máisculas e não digite números, ou aperte enter para voltar ao menu principal!')
                            erro_1 = False
                        if len(nome_cliente) >= 6 and not nome_cliente.isnumeric() and ex == 0:
                            nome.append(save_nome)
                            idade_cliente = input('Digite a idade do cliente: ')
                            erro_1 = True if idade_cliente < '18' or len(
                                idade_cliente) < 2 or not idade_cliente.isnumeric() and idade_cliente != '' else False
                            while erro_1:
                                idade_cliente = input(
                                    'Erro! Digite uma idade maior ou igual a 18 ou aperte para voltar ao menu principal: ')
                                erro_1 = False if idade_cliente.isnumeric() and idade_cliente >= '18' and len(
                                    idade_cliente) > 1 or idade_cliente == '' else True
                            if idade_cliente == '' and erro_1 == False:
                                nome.pop()
                                break
                            idade_cliente = int(idade_cliente)
                            idade.append(idade_cliente)
                            cpf_cliente = input('Digite o cpf do cliente: ')
                            erro_1 = True if not cpf_cliente.isnumeric() or len(cpf_cliente) > 11 or len(
                                cpf_cliente) < 11 or cpf_cliente in cpf else False
                            while erro_1:
                                cpf_cliente = input(
                                    'Erro! CPF inválido ou já cadastrado no sistema, digite um cpf válido ou digite 1 para voltar ao menu principal: ')
                                erro_1 = False if cpf_cliente.isnumeric() and len(
                                    cpf_cliente) == 11 and cpf_cliente not in cpf or cpf_cliente == '1' else True
                            if cpf_cliente == '1' and erro_1 == False:
                                idade.pop()
                                break
                            cpf.append(cpf_cliente)
                            cont += 1
                            voltar = input(
                                'Deseja cadastrar um novo cliente? Se sim digite s se não digite qualquer tecla: ')
                            if voltar == 's':
                                continue
                            else:
                                break

                elif tela_log == '2':
                    while opcao:
                        for x in range(cont):
                            print(f'Nome: {nome[x]}')
                            print(f'Idade: {idade[x]}')
                            print(f'CPF: {cpf[x]}')

                            print()
                        voltar = input('Digite enter ou qualquer tecla para sair: ')
                        opcao = False if voltar == '' else False

                elif tela_log == '3':
                    opcao = True
                    while opcao:
                        pesquisa = input('Digite o CPF do cliente que deseja buscar ou enter para voltar: ')
                        for indice, valor in enumerate(cpf):
                            if valor == pesquisa:
                                print(f'Nome: {nome[indice]}')
                                print(f'Idade: {idade[indice]}')
                                print(f'CPF: {cpf[indice]}')
                            else:
                                print(
                                    'Erro! Cliente não encontrado, favor digite um cpf válido e cadastrado no sistema!')
                        opcao = False if pesquisa == '' else True

                elif tela_log == '4':
                    opcao = True
                    while opcao:
                        excluir = input('Digite o Cpf do cliente no qual deseja excluir ou aperte enter para sair:')
                        opcao = False if excluir == '' else True
                        for indice, valor in enumerate(cpf):
                            if valor == excluir:
                                print(f'Nome: {nome[indice]}')
                                print(f'Idade: {idade[indice]}')
                                print(f'CPF: {cpf[indice]}')
                                excluir = input(
                                    'Deseja excluir o usuário acima? Se sim digite 1 se não digite qualquer tecla: ')
                                if excluir == '1':
                                    del (nome[indice])
                                    del (idade[indice])
                                    del (cpf[indice])
                                    print('Cliente excluido do sistema com sucesso!')
                            else:
                                print('Cliente não encontrado! Favor digite um CPF válido e cadastrado no sistema!')

                else:
                    logou = True
                    logado = False
                    print('Usuário deslogado do sistema!')

            log = False if logou == True or login == '' or senha == '' or retorno == '2' else True
    else:
        inicio = False
