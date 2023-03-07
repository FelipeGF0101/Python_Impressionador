"""
É possível retornar 2 "coisas"? 2 listas, 2 strings, 2 números...
Sim , basta retornar como uma tupla com 2 itens (vamos fazer um exemplo)

"""
def operacoes_basicas(num1, num2):
    soma = num1 + num2
    subt = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    return (soma, subt, mult, div)

print(operacoes_basicas(2, 5))