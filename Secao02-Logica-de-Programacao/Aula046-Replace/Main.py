string_com_ponto = '9.50'
string_com_virgula = '9,50'

print()
print(f'String com ponto: {string_com_ponto}')
print(f'String com vírgula: {string_com_virgula}')

# Como usar replace

print()
print(f"String com ponto para vírgula: {string_com_ponto.replace('.', ',')}")  # 9,50
print(f"String com vírgula para ponto: {string_com_virgula.replace(',', '.')}")  # 9.50
