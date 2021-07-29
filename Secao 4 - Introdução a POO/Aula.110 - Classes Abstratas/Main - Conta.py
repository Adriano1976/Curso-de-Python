'''
- O método abstrato é um contrato, você está basicamente informando que esse método não foi implementado
ainda e que precisa ser implementado nas subclasses. Ele é bastante usado em abstrações em geral e
padrões de projeto.
'''

from Conta_poupança import ContaPoupança
from Conta_corrente import ContaCorrente

CP = ContaPoupança('conta poupança', 111, 2550, 0)
CP.depositar(150)
CP.sacar(100)
CP.sacar(55)
CP.sacar(50)

print('#' * 60)

cc = ContaCorrente(tipoConta='conta corrente', agencia=4511, conta=333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(150)
cc.sacar(450)
cc.sacar(50)
cc.depositar(1575)
