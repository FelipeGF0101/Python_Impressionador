"""
Listas em python

Estrutura:

lista = [valor, valor, valor, valor, ...]

* Lista é um dos objetos mais importantes de Python, por isso vamos trabalhar bastante neles.
* Quando importamos uma base de dados para o python, normalmente ele é lido como uma "lista" ou como alguma "variação de lista"
* Listas em Python foram feitas para serem homogêneas, apesar de aceitarem valores heterogêneos
* Variáveis também aceitam variáveis
* Exemplos de Lista:

"""
# Listas de Produtos de uma loja:
produto = 'violão'
produtos = ['tv', produto,'celular', 'mouse', 'teclado', 'tablet']

# Lista de Unidades vendidas de cada produto da loja
vendas = [1000, 1500, 350, 270, 900]

print(produtos)

"""
lista[i] -> É o valor do índice da lista
OBS: Lembre que no python o índice começa em 0, então o primeiro item de uma lista é o item lista[0]

Para substituir um valor de uma lista você pode fazer:
lista[i] = novo_valor

"""
produtos1 = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
print(produtos1[1])

vendas1 = [1000, 1500, 350, 270, 900]
print(f"Vendas do produto {produtos1[1]} foram de {vendas1[1]} unidades.")