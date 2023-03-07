produtos = ['iphone', 'ipad', 'airpod', 'macbook']
precos = [7000, 10000, 2500, 14000]

# For item in lista
for preco in precos:
    print(preco * 1.1)
print()

# For i in range
for i in range(len(produtos)): # Dessa forma é possível saber o índice de cada item da lista
    produto = produtos[i]
    preco = precos[i]
    print(f'{produto} >> {preco}')
print()

# For item ins lista com enumerate

for i, preco in enumerate(precos):
    preco = preco * 1.1
    produto = produtos[i]
    print(produto, preco)