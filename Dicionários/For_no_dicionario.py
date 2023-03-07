"""
For nos dicionários

Estrutura:

for chave in dicionário:
faça alguma coisa

"""
vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#demonstrando o for
for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]} Unidades')


total_notebook = 0

for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]} Unidades')
    if 'notebook' in chave:
        total_notebook += vendas_tecnologia[chave]

print()

print(f'O total de notebooks é: {total_notebook}')