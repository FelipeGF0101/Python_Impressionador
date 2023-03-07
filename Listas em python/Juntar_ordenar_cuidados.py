"""
Juntar listas, ordenar e cuidados especiais

2 formas:
lista1.extend(lista2)
lista_nova = lista1 + lista2

OBS: O método append não junta listas, mas adiciona um valor no final da lista

"""

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']

print(len(produtos))
print()
produtos.extend(novos_produtos)
print(produtos)
print()
print(len(produtos))
print()

# Também poderia ser:
todosProdutos = produtos + novos_produtos
print(todosProdutos)
print()

# Utilizando append() : O append() adiciona outra lista na lista como se fosse um único valor.
produtos.append(novos_produtos)
print(produtos)
print()

# CUIDADO 
# [1] + [2] não é o mesmo que 1 + 2, então cuidado sempre com o formato dos valores na hora de fazer operações.

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

total_iphone = vendas[2] + vendas[3]
print(total_iphone)
print()

# Diferente de:
total_iphone_listas = vendas_iphonex + vendas_iphone11
print(total_iphone_listas)
print()

# Também poderia ser:
total = vendas_iphonex[0] + vendas_iphone11[0] # Somando os únicos valores das listas utilizando o índice
print(total)
print()

# ORDENAR LISTA 

# lista.sort()
produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']
produtos.sort()
print(produtos)
print()

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas.sort()
print(vendas)
print()

# Ordenando de forma decrescente
vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas.sort(reverse=True)
print(vendas)

