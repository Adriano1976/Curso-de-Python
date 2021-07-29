numero = input("Digite o seu CPF: ")
print(f'CPF Digitado: {numero}')

numero1 = numero[:-2]
a = 10
c = 0

# Aqui a checagem dos 11 digitos
if not numero1.isnumeric() or len(numero) != 11:
    print("O CPF só pode conter numeros.")
    print("Digite exatamente 11 caracteres.")
else:
    for cpf in numero1:
        b = int(cpf) * a
        a -= 1
        c = c + b

    conta = 11 - (c % 11)

    if conta > 9:
        digito1 = 0
    else:
        digito1 = conta

    # Adicionado o primeiro digito encontrado
    numero1 = f'{numero1}{digito1}'

    c = 0
    a = 11

    for cpf2 in numero1:
        b = int(cpf2) * a
        a -= 1
        c = c + b

    conta = 11 - (c % 11)

    # Digito 2
    if conta > 9:
        digito2 = 0
    else:
        digito2 = conta

    # Agora é só adicionar o dígito 2
    resultado = f'{numero1}{digito2}'

    if numero == resultado:
        print(f"O seu CPF {resultado} é válido.")
    else:
        print(f"O seu CPF {numero} não é válido.")
