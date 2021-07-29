""" Operador terário em Python """

# Exemplo de uma operação NÃO ternário

logged_user = False
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'
print(msg)

# Exemplo de uma operação ternário

usuario_logado = False
mensagem = 'Usuáro Logado.' if usuario_logado else 'Usuário precisa logar.'
print(mensagem)

idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    mensagem = 'Pode acessar' if maior_idade else 'Não pode acessar.'
    print(mensagem)
