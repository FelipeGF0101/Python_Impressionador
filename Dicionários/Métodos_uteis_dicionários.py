"""
Métodos úteis em dicionários

items() dos dicionários

Estrutura:

itens_dicionário = dicionário.items()

ou então:

for item in dicionário.items()
    cada item do dicionario em formato de tupla

"""
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}
# O items() transforma um dicionário em uma lista de tuplas

itens_dicionario = vendas_tecnologia.items()
print(itens_dicionario)
print()

# OU

for item in vendas_tecnologia.items():
    print(item)
print()

# OU

for produto, qtde in vendas_tecnologia.items():
    print(f"{produto}: {qtde}")
print()
# - Quais produtos venderam mais de 5000 unidades?

#forma 1 -> usando apenas o dicionario e as chaves
for item in vendas_tecnologia:
    if vendas_tecnologia[item] > 5000:
        print(f'{item}: {vendas_tecnologia[item]} vendas.')
print()

#forma 2 -> usando o dicionario.items()
for mercadoria, vendas in vendas_tecnologia.items():
    if vendas > 5000:
        print(f'{mercadoria}: {vendas} Vendas')

print()

"""
# LISTAS IMPORTANTES A PARTIR DO DICIONÁRIO

# Métodos importantes:

.keys() -> uma "lista" com todas as chaves do dicionario

.values() -> uma "lista" com todos os valores do dicionario

Obs: Se o dicionario for modificado, automaticamente essas variáveis são modificadas, mesmo tendo sido criadas anteriormente

"""
chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)
print(valores)
print()
"""
 O FOR VAI FUNCIONAR NORMAL EM DICT_LISTAS, PORQUE NÃO DEIXA DE SER UMA LISTA DE ITENS QUE PODE SER PERCORRIDA (ITERABLE), MAS
O QUE APRENDEMOS DE LISTA NÃO NECESSARIAMENTE SE APLICAM A ESSAS DICT_LISTAS.

PARA TRANSFORMAR AS DICT_LISTAS EM LISTAS NORMAIS, USAMOS A FUNÇÃO LIST:

* LIST_CHAVES = LIST(DICIONARIO.KEYS())
* PODE SER ÚTIL CASO A GENTE QUEIRA FAZER ALGUMA ORGANIZAÇÃO DAS CHAVES. EX: IMPRIMIR UMA LISTA COM OS VALORES EM ORDEM ALFABÉTICA,
DE FORMA QUE TODAS AS TVS FIQUEM JUNTAS, TODOS OS IPHONE/IPAD TAMBÉM E ASSIM VAI:

"""
print(list(chaves))
print(list(valores))
print()

for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades')
print('-' * 40)

# Agora pra organizar essas informações
lista_chaves = list(chaves)
lista_chaves.sort()

for chave in lista_chaves:
    print(f"{chave}: {vendas_tecnologia[chave]}")