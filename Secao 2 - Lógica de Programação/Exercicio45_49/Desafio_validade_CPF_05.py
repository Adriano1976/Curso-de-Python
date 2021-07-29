while True:
    print(f'{"VALIDADOR DE CPF":^20}')
    total_digito1 = 0
    total_digito2 = 0

    numero = input('Digite o seu CPF (x para sair): ').upper().strip()
    if numero == 'X':
        print('Finalizando...')
        break

    while not numero.isnumeric() or len(numero) != 11:
        numero = input('ERRO! Digite APENAS 11 dígitos númericos: ')
    cpf = list(numero)
    cpfjunto = ''.join(cpf)  # juntei o cpf para mostrar fora da lista

    print(f'CPF digitado: {cpfjunto}')

    #####################
    ## CHECA SEQUENCIA ##
    #####################
    sequencia = cpfjunto[0] * len(cpfjunto)

    if sequencia == cpfjunto:
        print("\nCPF É UMA SEQUÊNCIA DE DIGITOS\n")
        continue
    # FIM DA CHECAGEM DE SEQUÊNCIA

    # total pra descobrir o digito 1
    contador = 10
    for numero in cpf[0:9]:
        numero = int(numero)
        resultado1 = numero * contador
        total_digito1 += resultado1
        if contador == 2:
            break
        contador -= 1

    # total pra descobrir o digito 2
    contador2 = 11
    for numero in cpf[0:10]:
        numero = int(numero)
        resultado2 = numero * contador2
        total_digito2 += resultado2
        if contador2 == 2:
            break
        contador2 -= 1

    novo_cpf = list(cpfjunto)  # aqui eu criei uma nova lista a partir da variavel cpfjunto

    ##### DIGITO 1
    digito1 = 11 - (total_digito1 % 11)
    if digito1 > 9:  # aqui eu verifico se o digito1 é > 9
        del (novo_cpf[9])  # aqui o 1º digito verificador errado é deletado
        digito1 = '0'
        novo_cpf.insert(9, digito1)  # aqui o novo 1º digito verificador é inserido
    else:  # aqui eu verifico se o digito1 é <= 9
        del (novo_cpf[9])
        digito1 = str(digito1)
        novo_cpf.insert(9, digito1)

    #### DIGITO 2
    digito2 = 11 - (total_digito2 % 11)
    if digito2 > 9:
        del (novo_cpf[10])  # aqui o 2º digito verificador errado é deletado
        digito2 = '0'
        novo_cpf.insert(10, digito2)  # aqui o novo 2º digito verificador é inserido
    else:
        del (novo_cpf[10])
        digito2 = str(digito2)
        novo_cpf.insert(10, digito2)

    if cpf == novo_cpf:  # aqui é comparado o cpf antigo com o novo cpf (tendo os dois ultimos digitos corrigidos)
        print(f'O CPF: {cpfjunto} é VÁLIDO!')
    else:
        print(f'O CPF: {cpfjunto} é INVÁLIDO!')
    print()