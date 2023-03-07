"""
Copiar e "Igualdade" de listas

Estrutura:
Quando fazemos:
lista2 = lista1
Não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.

Se quisermos copiar lista devemos fazer:
lista2 = lista1.copy()
ou então:
lista2 = lista1[:]

"""

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista
print(lista)
print(lista2)
print()

lista[1] = 'iphone 11'

print(lista)
print(lista2)
print()

# AGORA COPIANDO

lista3 = ['ipad', 'iphone x', 'apple tv']
lista4 = lista3.copy()
print(lista3)
print(lista4)
print()

lista3[1] = 'iphone 11'

print(lista3)
print(lista4)
print()

# OUTRA FORMA DE COPIAR LISTA
lista5 = ['ipad', 'iphone x', 'apple tv']
lista6 = lista5[:]

print(lista6)