"""
Algumas funções básicas de lista

Tamanho da lista

tamanho = len(lista)

"""
produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']

# Quantos produtos tempos a venda?
tamanho = len(produtos)
print(tamanho)
"""
MAIOR E MENOR VALOR

maior = max(lista)
menor = min(lista)

"""

vendas = [1000, 1500, 15000, 270, 900, 100, 1200]

# Qual é o item mais vendido?
# Qual é o item menos vendido?

maior = max(vendas)
menor = min(vendas)
print(maior)
print(menor)
print()


maisVend = vendas.index(max(vendas))
produto = produtos[maisVend]
print(f'O produto mais vendido foi o {produto} com {max(vendas)} unidades.')
print()

menosVend = vendas.index(min(vendas))
produtob = produtos[menosVend]
print(f'O produto menos vendido foi o {produtob} com {min(vendas)} unidades vendidas.')