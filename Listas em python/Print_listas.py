"""
2 opções:

print("normal")
método join -> texto.join(lista)

"""
produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']
print(produtos)
# resultado: ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']
print()

print(', '.join(produtos))
# resultado: apple tv, mac, iphone x, iphone 11, ipad, apple watch, mac book, airpods
print()

# Caso eu queira imprimir tudo em linhas diferentes
print(';\n'.join(produtos))
# Resultado:
# apple tv;
# mac;
# iphone x;
# iphone 11;
# ipad;
# apple watch;
# mac book;
# airpods
print()

# Lembrando do método split de strings:

# lista = texto.split(separador)
produtos = 'apple tv, mac, iphone x, iphone 11, ipad, apple watch, mac book, airpods'
lista = produtos.split(',')
print(lista)
# Resultado:
# ['apple tv', ' mac', ' iphone x', ' iphone 11', ' ipad', ' apple watch', ' mac book', ' airpods']
# O resultado acima ainda ficou um espaço entre os itens.
print()

produtos = 'apple tv, mac, iphone x, iphone 11, ipad, apple watch, mac book, airpods'
lista = produtos.split(', ')
print(lista)
# Resultado:
# ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']
# Sem espaços 