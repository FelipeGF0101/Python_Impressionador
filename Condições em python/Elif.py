"""
ELIF

E se temos mais do que um caso de sim e não?

E se tivermos 3 casos?

Exemplo:

Vamos criar um programa para analisar o bônus dos funcionários de uma empresa (pode parecer "Simples", mas uma empresa como a Amazon tem 900.000 funcionários)

Para os cargos de vendedores, a regra do bônus é de acordo com a meta de vendas da pessoa: 

* Se ela vendeu abaixo da meta dela, ela não ganha bônus.
* Se ela vendeu acima da meta dela, ela ganha como bônus 3% do que ela vendeu.
* Se ela vendeu mais do que o dobro da meta dela, ela ganha como bônus 7% do valor que ela vendeu.

Vamos criar um programa para avaliar uma pessoa que tinha como meta de vendas 20.000 reais e calcular o bônus dela de acordo com o valor que ela tiver.
"""
meta = 20000
vendas = float(input("Informe o valor de vendas feitas por você: "))

if vendas < meta:
    print(f"Infelizmente você não atingiu a meta. Suas vendas foram no valor de R$ {vendas}")
elif vendas >= meta and vendas < (meta * 2):
    print(f"Parabéns! Você receberá um bônus de 3% do valor total de suas vendas! O valor é de R${ 0.03 * meta:.2f}")
elif vendas > (meta * 2):
    print(f"Parabéns! Você teve um excelente rendimento. Seu bônus será de 7% do valor total de suas vendas! O valor é de R$ {0.07 * meta:.2f}")

    
