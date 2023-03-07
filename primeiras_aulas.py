"""Variáveis"""

#quant_vendas = 1500
#print(quant_vendas)

# ================
# Calculo com variáveis
#faturamento = 150
#custo = 60

#lucro = faturamento - custo
#print(lucro)

# ==================
# Entrada de dados com input

#nome = input('Qual é o seu nome? ')

#print(nome)

#nome: str = input('Qual é o seu nome? ')
#sobrenome: str = input('Qual é o seu sobrenome? ')

#print(nome + ' ' + sobrenome)
#print(f'{nome} {sobrenome}')
# =================
# EXERCÍCIO

"""
Exercício do módulo 1 - Operações, Variáveis e input

Parte 1 - Operações e variáveis

Crie um programa que imprima (print) os principais indicadores da loja Hashtah&Drink no último ano. Obs: faça tudo usando variáveis.
Valores do último ano:
-Quantidade de vendas de coca = 150
-Quantidade de vendas de pepsi = 130
-Preço unitário da coca = 1,50
-Preço unitário da pepsi = 1,50
-Custo da loja = 2.500,00
"""
qtd_Vcoca = 150
qtd_Vpepsi = 130
prç_uni_coca = 1.50
prç_uni_pepsi = 1.50
custo_loja = 2500

# Qual foi o faturamento de pepsi da Loja?

fatu_pepsi = qtd_Vpepsi * prç_uni_pepsi

print(f'A loja faturou R$ {fatu_pepsi:.2f} com a pepsi.')

print()

# Qual foi o faturamento da coca na Loja?

fatu_coca = qtd_Vcoca * prç_uni_coca
print(f'A loja faturou R$ {fatu_coca:.2f} com a coca.')

# Qual foi o lucro da loja?

lucro = fatu_coca + fatu_pepsi - custo_loja
print(lucro)

# Qual foi a marem da loja? (marem = lucro / faturamento )
print(lucro/(fatu_coca + fatu_pepsi))

# PARTE 2 - Inputs e Strins

"""A maioria das empresas trabalham com um código para cada produto que possuem. A hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.Ex: 

Coca -> Cógigo: BEB1300543
Pepsi -> Cógio: BEB1300545
Vinho Primitivo Lucarello -> Código: BAC1546001
Vodka Smirnoff -> BAC17675002

Repare que todas as bebidas não alcóolicas têm o início do código "BEB" e todas as bebidas alcóolicas têm o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

"""
codigo = input('Qual é o código da bebida? (Insira tudo em letra maiúscula): ')
print('BAC' in codigo)
