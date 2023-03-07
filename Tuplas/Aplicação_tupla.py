"""
Aplicação de Tupla - Lista de Tuplas

Estrutura:

Além de casos como o do enumerate, em que usamos uma função para transformar itens em tuplas porque isso ajuda o nosso código, temos também listas de tuplas
como algo comum dentro do Python.

lista = [
    tupla1,
    tupla2,
    tupla3,
    ]
    
ou seja

lista = [
    (valor1, valor2, valor3),
    (valor4, valor5, valor6),
    (valor7, valor8, valor9),
    ]

"""
# Exemplo:

# Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.

# Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# Forma 1
faturamento = vendas[0][4] * vendas[0][5]
print(faturamento)
print()

# Forma 2 - com unpacking
data, produto, cor, capacidade, unidades, valor_unitario = vendas[0]
faturamento = unidades * valor_unitario
print(faturamento)
print()


# Qual foi o faturamento do Iphone no dia 20/08/2020?
faturamento1 = 0
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento1 += unidades * valor_unitario

print(f'{faturamento1:.2f}')
print()

# Qual foi o produto mais vendido (em unidades) no dia 21/08/2020
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if data == '21/08/2020':
        maior = 0
        mais_vendido = ''
        maior_capacidade = ''
        if unidades > maior:
            maior_capacidade = capacidade
            mais_vendido = produto
            maior = unidades

print(f'O produto mais vendido foi {produto} com capacidade de {maior_capacidade}, com um total de {maior} vendas')