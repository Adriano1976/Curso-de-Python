cpf = '16899535009'
novo_cpf = cpf[:-2]
soma1 = 0
soma2 = 0

for e, r in enumerate(range(10, 1, -1)):
    soma1 = soma1 + int(novo_cpf[e]) * int(r)
    digito_1 = 11 - (soma1 % 11)

if digito_1 > 9:
    digito_1 = 0
novo_cpf += str(digito_1)

for e, r in enumerate(range(11, 1, -1)):
    soma2 = soma2 + int(novo_cpf[e]) * int(r)
    digito_2 = 11 - (soma2 % 11)

if digito_2 > 9:
    digito_2 = 0
novo_cpf += str(digito_2)

if novo_cpf == cpf:
    print("Cpf valido!")
else:
    print("Cpf invalido!")
