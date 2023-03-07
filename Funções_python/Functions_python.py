"""
Function em python

O que é?

As functions são blocos de código que servem a 1 único propósito, fazem uma ação especifica.

ESTRUTURA BÁSICA

def nome_funcao():
    faca alguma coisa 
    faca outra coisa
    return valor_final

Exemplo: Vamos criar uma função de cadastro de um produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.




lista = [150, 10, 30, 2000, 90]

# Exemplo de função: .sort()
lista.sort()
print(lista)
print()

# Criando a própria função

def cadastrar_produto():
    produto = input("Digite o nome do produto que deseja cadastrar: ")
    produto = produto.casefold()
    print(f"Produto {produto} cadastrado com sucesso")

# Executando a função:
cadastrar_produto()

# Utilizando a função dentro de um for:

for i in range(3):
    cadastrar_produto()
"""
# Treinando
nome = []
def cadastrar_nome():
    nome1 = input('Insira um nome: ').upper()
    nome.append(nome1)

for item in range(4):
    cadastrar_nome()

def mostrar_nome(lista):
    for item in nome:
        print(f'{item}')

mostrar_nome(nome)



