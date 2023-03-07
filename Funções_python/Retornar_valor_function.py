"""
Estrutura básica:

def nome_funcao():
    return valor_final

* Exemplo: vamos criar uma função de cadastro de um produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.



def cadastrar_produto():
    produto = input("Digite o nome do produto que deseja cadastrar: ")
    produto = produto.casefold()
    produto = produto.strip()
    return produto
# return vai retornar o valor da função. (nesse caso o valor que está sendo introduzido pelo input)
# Mas deve ser usado uma outra variável para receber o valor da funcão/return. (nesse caso foi usado a variável -> variavel_produto)
lista = []
for i in range(3):
    variavel_produto = cadastrar_produto()
    lista.append(variavel_produto)

print(lista)
"""

def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar: ')
    produto = produto.upper()
    produto = produto.strip()
    return produto

produto = cadastrar_produto()

print(produto)