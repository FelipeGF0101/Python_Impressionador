"""
Adicionar e remover itens da lista

Adicionar:
lista.append(item)

Remover:
item_removido = lista.pop(indice) # Aqui existe a opção de armazenar em uma outra variável, o item removido.
lista.remove(item)

"""
# Digamos que você está construindo o controle de produtos da Apple.
# E a Apple lançou o Iphone 11 e irá tirar dos seus estoques o Iphone X.

produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']
print(produtos)
# Trocar:
#produtos[2] = 'iphone 11'
#print(produtos)

# ====================================

# Adicionar o iphone 11:
produtos.append('iphone 11')
print(produtos)
print()
# ====================================

# Remover o Iphone x
# Com remove()
produtos.remove('iphone x')
print(produtos)

# ====================================

# Remover o Ipad
# Com pop()
# Forma 1
produtos.pop(2)
print(produtos)

# Forma 2
# removido = produtos.pop(2)
# print(removido)

# EXISTEM DUAS FORMAS DE TRATAR O ERRO
# 1 - Criar um if para evitar que ele aconteça
# 2 - Esperar que ele possa acontecer e tratar caso o erro aconteça com:

# try:
#   tentar fazer
# except:
#   caso dê errado

try:
    produtos.remove('iphonex')
except:
    print("Iphonex não existe na lista de produtos")

# outra forma

try: 
    produtos.remove('iphone x')
    print(produtos)
except:
    pass