"""
Transformando Listas em Dicionários e Function zip

Estrututa: 

* Dicionário com valores padrões:

EXEMPLO 1 = Dicionário =  dict.fromkeys(lista_chave, valor_padrão)

* Dicionário a partir de listas de tuplas

EXEMPLO 2 = Dicionário = dict(lista_tuplas)


EXEMPLO 3

* Dicionário a partir de 2 listas:

Passo 1: Tranformar listas em lista de tuplas com o método zip 
Passo 2: Transformar em dicionário

lista_tuplas = zip(lista1, lista2)dicionário = dict(lista_tuplas)
"""

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]


# Quanto vendemos de IPAD?

# fazendo por listas
# fazendo por dicionario 

# EXEMPLO 1:

dicionario = dict.fromkeys(produtos, 0)
print(dicionario)
print()

# Forma para verificar cada item:

#lista_tuplas = zip(produtos, vendas)
#for item in lista_tuplas:
#    print(item)

# EXEMPLO 2/ EXEMPLO 3
lista_tuplas = zip(produtos, vendas)
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)

# VERIFICANDO A MELHOR FORMA DE TRABALHAR
# 1 - FAZENDO POR LISTAS:
indice = produtos.index('ipad')
print(f'O produto Ipad teve {vendas[indice]} vendas')

# 2 - FAZENDO POR DICIONÁRIO:
print(f'Vendemos {dicionario_vendas["ipad"]} Ipads')