"""
Usando módulos para ajudar a resolver desafios

Objetivo

* Muitas vezes algum módulo vai ajudar a gente a resolver um desafio que talvez até conseguissemos resolver de outra forma.

Exemplo
Digamos que você está analisando todas as vendas dos produtos de tecnologia de um e-commerce e quer saber quais foram os 5 produtos que mais venderam (e suas
respectivas quantidades de vendas) - ou seja, queremos decobrir um top 3 produtos de forma simples.
"""
from collections import Counter
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

aux = Counter(vendas_tecnologia)
print(aux.most_common(5))



