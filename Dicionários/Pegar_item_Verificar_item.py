"""
Não confie na ordem dos dicionários, usar as chaves

Python Versões antigas x Versões novas

* Dicionários eram "sem ordem". Atualmente tem ordem, mas o certo é usar as chaves.
* 2 formas de pegar um valor:
    * dicionario[chave]
    * .get(chave)


"""

mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
print(f'O livro mais vendido foi {mais_vendidos["livros"]}')
print(f'O livro mais vendido foi {mais_vendidos["lazer"]}')

# Quanto foi vendido de notebook asus e de ipad
# Utilizando o método .get
print(vendas_tecnologia.get('notebook asus'))
print(f'vendemos {vendas_tecnologia.get("ipad")} ipads ')

# Se o método .get não encontrar nada no dicionário com o nome da chave fornecido, ele retorna none.

if 'copo' in vendas_tecnologia:
    print(vendas_tecnologia['copo'])
else:
    print('Copo não está dentro da lista de produtos de tecnologia')

# Outra forma 
if vendas_tecnologia.get('copo') == None:
    print('Copo não está dentro da lista de produtos de tecnologia')
else:
    print(vendas_tecnologia.get('copo'))