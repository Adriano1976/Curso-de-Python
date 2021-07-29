''' Iterando string com while em Python '''

frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
nova_string = ''
contador = 0

print('\no rato roeu a roupa do rei de roma')
input_do_usuario = input('Digite a letra que deseja mudar para maiúscula: ')

while contador < tamanho_frase:  # Iteração / Iterar
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
