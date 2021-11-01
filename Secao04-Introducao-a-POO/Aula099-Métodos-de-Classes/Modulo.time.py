import time

print('=-' * 70)
print(time.localtime())  # Retorna a data e hora local no formato de uma estrutura chamada "struct_time"
print(time.asctime())  # Retorna a data e hora como string, conforme a configuração do sistema operacional.
print(time.time())  # Retorna o tempo do sistema em segundos.
