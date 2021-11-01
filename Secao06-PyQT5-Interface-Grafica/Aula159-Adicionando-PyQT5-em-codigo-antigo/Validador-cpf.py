while True:
    print('Informe:\n1 - CPF\n0 - Sair')
    opcao = input('Opção: ')

    # Checks if the value is really numeric and if it has 1 digit.
    if not opcao.isnumeric() or len(opcao) != 1:
        print('\nOpção inválido.\nInforme a opção correta.\n')
        continue

    if opcao == '0':
        print('\nPrograma finalizado.')
        break

    if opcao == '1':
        cpf = input('Digite CPF: ')
        novo_cpf = cpf[:-2]  # Delete the last two digits of the CPF
        reverso = 10  # Reverse counter.
        total = 0

        # Checks if the value is really numeric and if it has 11 digits.
        if not cpf.isnumeric() or len(cpf) != 11:
            print('\nValor inválido.\nInforme o cpf com 11 digitos.\n')
            continue

        for index in range(19):  # Loop do CPF
            if index > 8:  # First index goes from 0 to 9.
                index -= 9  # These are the first 9 digits of the CPF.

            total += int(novo_cpf[index]) * reverso  # Total amount of multiplication.

            reverso -= 1  # # Decrements the reverse counter.
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:  # If the digit is > 9 the value is 0.
                    d = 0
                total = 0  # Reset the total.
                novo_cpf += str(d)  # Concatenate the digit generated in the new cpf.

        # Avoid sequential digits. E.g.: 11111111111, 00000000000...
        sequency = novo_cpf == str(novo_cpf[0]) * len(cpf)

        if cpf == novo_cpf and not sequency:
            print(f'CPF Válido: {novo_cpf}\n')
        else:
            print(f'CPF Inválido: "{cpf}"\n')
