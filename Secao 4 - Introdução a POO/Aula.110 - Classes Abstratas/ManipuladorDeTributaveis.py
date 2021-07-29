from Tributavel import ContaCorrente, SeguroDeVida


class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total


if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João Carlos', 1000.0)
    seguro = SeguroDeVida(100.0, 'Roberto', 345 - 77)

    print(cc.get_valor_imposto())
    print(seguro.get_valor_imposto())
