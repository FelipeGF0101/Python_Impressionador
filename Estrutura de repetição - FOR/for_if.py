"""
for + if

Estrutura:
for item in lista:
    if condicao:
        faça alguma coisa
    else:
        outra coisa

"""
# Digamos que a gente esteja analisando a meta de vendas de vários funcionários de uma empresa. A meta de vendas é de 1000 em 1 dia.
# Temos uma lista com as vendas de todos os funcionários e quero calcular qual o % de pessoas que bateram a meta.

vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000
cont = 0
for item in vendas:
    if item >= meta:
        cont += 1
    else:
        pass

print(f'O percentual é de {cont / len(vendas):.1%} ')