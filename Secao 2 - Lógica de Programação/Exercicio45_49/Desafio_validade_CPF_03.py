cpf = input('Digite um CPF no formato ***.***.***-**: ')

sep_dig = cpf.split('-')
sem_dig = sep_dig[0]

sep_ponto = sem_dig.split('.')
sem_ponto = ''.join(sep_ponto)

soma = 0
c = 0

# Aqui a checagem dos 11 digitos
for i in sem_ponto:
    a = int(i)
    b = (10 - c)
    soma += a * b
    c += 1

formula = 11 - (soma % 11)
d1 = '0' if formula > 9 else str(formula)
com_d1 = sem_ponto + d1

soma2 = 0
c2 = 0
for i in com_d1:
    a = int(i)
    b = (11 - c2)
    soma2 += a * b
    c2 += 1

formula2 = 11 - (soma2 % 11)
d2 = '0' if formula2 > 9 else str(formula2)
dig = d1 + d2

cpf_final = sem_ponto + d1 + d2

if cpf_final == cpf[0] * 11:
    print(f'{cpf} NÃO é um CPF válido!')
elif dig == sep_dig[1]:
    print(f'{cpf} É um CPF válido!')
else:
    print(f'{cpf} NÃO é um CPF válido!')