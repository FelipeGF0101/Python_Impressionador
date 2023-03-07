"""
Utilidade:

Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

Esrutura:

*args para positional arguments -> argumentos vem em formato de tupla

def minha_funcao(*args):
    ...

**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):
    ...
"""
def minha_funcao(*args): # *args vai te permitir adicionar um número ilimitado de argumentos na função
    soma = 0
    for numero in args:
        soma += numero
    return soma

print(minha_funcao(10, 20 , 30, 5))
print()

def preco_final(preco,**kwargs):
    if 'desconto' in kwargs:
        preco *= (1 - kwargs['desconto'])
    if 'garantia_extra' in kwargs:
        preco += kwargs['garantia_extra']
    if 'imposto' in kwargs:
        preco *= (1 + kwargs['imposto'])
    return preco

print(preco_final(1000, desconto=0.2, garantia_extra=100, imposto=0.06))

