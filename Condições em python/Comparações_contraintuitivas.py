"""
Comparações contraintuitivas

Existem alguma comparações no python que não são intuitivas quando vemos pela primeira vez, mas que são muito usadas, principalmente por programadores mais experientes.

É bom sabermos alguns exemplos e buscar sempre entender o que aquela comparção está buscando verificar.

Exemplo1:

Digamos que você está construindo um sistema de controle de vendas e precisa de algumas informações para fazer o cálculo do resultado da loja no fim de um mês.

"""
faturamento  = input("Qual foi o faturamento da loja nesse mês? ")
custo = input("Qual foi o custo da loja nesse mês? ")

if faturamento == '' or custo == '':
    print("Preencha o faturamento e o custo corretamente")
else:
    lucro = int(faturamento) - int(custo)
    print(f"O lucro da loja foi de R$ {lucro} reais. ")

# ou

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f"O lucro da loja foi de R$ {lucro} reais. ")
else:
    print("Preencha o faturamento e o custo corretamente!")