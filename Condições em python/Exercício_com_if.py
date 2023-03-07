"""
Cálculo de bônus 
 
* Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas. Caso contrário, o valor do funcionário é 0.

Print o bônus dos 3 funcionários.

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

"""
meta = 1000
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= meta:
    print(f"O funcionário 1 irá receber R$ {vendas_funcionario1 * 0.10} de bônus.")
else:
    print(f"O funcionário 1 receberá R$ 0.00 de bônus.")

if vendas_funcionario2 >= meta:
    print(f"O funcionário 2 irá receber R$ {vendas_funcionario2} de bônus.")
else:
    print(f"O funcionário 2 receberá R$ 0.00 de bônus.")

if vendas_funcionario3 >= meta:
    print(f"O funcionário 3 irá receber R$ {vendas_funcionario3 * 0.10} de bônus.")
else: 
    print(f"O funcionário 1 receberá R$ 0.00 de bônus.")
print()
"""
Cálculo de bônus com uma nova regra

Agora crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas
Agora os funcionário que venderem muiito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:

* Se as vendas do funcionário forem maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas.
* Se as vendas do funcionário forem menor que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas.
* Se as vendas forem menor do que 1000, então o bônus do funcionário é de R$ 0.00

"""
venda_funci1 = 1000
venda_funci2 = 770
venda_funci3 = 2700

if venda_funci1 >= 2000: 
    bonus = venda_funci1 * 0.15
elif venda_funci1 >= 1000:
    bonus = venda_funci1 * 0.10
elif venda_funci1 < 1000:
    bonus = 0
print(f"O funcionário 1 receberá R$ {bonus} de bônus.")
print()

if venda_funci2 >= 2000: 
    bonus = venda_funci2 * 0.15
elif venda_funci2 >= 1000:
    bonus = venda_funci2 * 0.10
elif venda_funci2 < 1000:
    bonus = 0
print(f"O funcionário 2 receberá R$ {bonus} de bônus.")
print()

if venda_funci3 >= 2000: 
    bonus = venda_funci3 * 0.15
elif venda_funci3 >= 1000:
    bonus = venda_funci3 * 0.10
elif venda_funci3 < 1000:
    bonus = 0
print(f"O funcionário 3 receberá R$ {bonus} de bônus.")