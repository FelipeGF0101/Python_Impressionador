"""
FOR "EACH"

O for no Python consegue percorrer uma lista e a cada "loop" retornar o valor do item.

for i in range(5):
    print(i)

range(5) é na verdade uma lista do tipo: [0, 1, 2, 3, 4]


USANDO PARA LISTAS:

for item in lista:
    print(item)

ou então para string:

for ch in texto:
    print(ch)

"""
produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
texto = 'lira@gmail.com'

for i in range(5):
    print(produtos[i])

# percorrendo uma string com for
for ch in texto:
    print(f'{ch:>10}')