from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

print(p1.get_ano_nascimento())
print(p1.get_ano_nascimento())
print(p1.falar('o evangelho de Jesus Cristo'))
print(p1.comer('cuscuz com ovo'))
print(p1.parar_falar())
print(p1.comer('pão com presunto e queijo'))
print(p1.falar('o jantar'))
print(p1.parar_comer())
print(p1.comer('lazanha'))

p1.parar_comer()
p1.parar_falar()



