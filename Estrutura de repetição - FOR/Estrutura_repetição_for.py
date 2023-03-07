"""
Estrutura de repetição - FOR

Funcionamento

for i in range(n)
    repetir código n vezes

for i in range(5):
    print(i)
"""

# Imagine que você está construindo uma automação para enviar todo dia  por email um resumo da produção de uma fábrica.
# Construa um código que exiba a quantidade produzida de cada produto nesse email.

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for produto in produtos:
    i = produtos.index(produto)
    print(f"Os produtos tiveram os seguintes números de produção: {produto} -> {producao[i]} unidades. ")
print()

#Solução alternativa
for i in range(5):
    print(f"{produtos[i]}, {producao[i]}")
print()

# Solução alternativa 2:
for i in range(len(produtos)):
    print(f"{produtos[i]}, {producao[i]}")