"""
Dicionários em Python

Estrutura:
dicionário: {chave: valor, chave: valor}

vantagens e desvantagens:
Não devem ser usados para pegar itens em uma determinada ordem
Podem ter valores heterogêneos (vários tipos de valores dentro de um mesmo dicionário: inteiros, strings, listas, etc)
Chaves são únicas obrigatoriamente
Mais intuitivos de trabalhar

"""
mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Acessando uma informação no dicionário pela chave.
qtde_iphone = vendas_tecnologia['iphone']
print(qtde_iphone)

# Qual foi o item mais vendido nas categorias 'livors' e 'lazer'?
livro = mais_vendidos['livros']
lazer = mais_vendidos['lazer']
print(livro)
print(lazer)

# Quanto foi vendido de notebook asus e de ipad?
qtde_noteasus = vendas_tecnologia['notebook asus']
qtde_ipade = vendas_tecnologia['ipad']
print(qtde_ipade)
print(qtde_noteasus)