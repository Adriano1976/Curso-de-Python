
def aumento(valor, porcentagem, formata=False):
    var = valor + (valor * (porcentagem / 100))

    if formata:
        return formata.real(var)
    else:
        return var


def reducao(valor, porcentagem, formata=False):
    var = valor - (valor * (porcentagem / 100))

    if formata:
        return formata.real(var)
    else:
        return var
