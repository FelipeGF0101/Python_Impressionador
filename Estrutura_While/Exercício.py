"""
EXERCÍCIO

Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.

O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem ter digitado nenhum produto ou quantidade.

Ao final do programa ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha. Sugestão para sua lista de produtos vendidos:

vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]
"""
# FORMA 1
vendas = []

while True:
    produto = input('Qual é o produto? ')
    if not produto:
        break
    qtde = int(input('Qual a quantidade? '))
    vendas.append([produto, qtde])
print(vendas)
print()

# FORMA 2
vendas = []
produto = input('Qual é o produto? ')
qtde = int(input('Qual a quantidade? '))

while produto:
    vendas.append([produto, qtde])
    produto = input('Qual é o produto? ')
    qtde = int(input('Qual a quantidade? '))
    
print(vendas)