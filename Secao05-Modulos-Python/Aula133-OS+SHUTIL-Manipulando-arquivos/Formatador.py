def formate(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = tamanho
        text = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        text = 'K'
    elif tamanho < giga:
        tamanho /= mega
        text = 'M'
    elif tamanho < tera:
        tamanho /= giga
        text = 'G'
    elif tamanho < peta:
        tamanho /= tera
        text = 'T'
    else:
        tamanho /= peta
        text = 'p'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{text}'.replace('.', ',')