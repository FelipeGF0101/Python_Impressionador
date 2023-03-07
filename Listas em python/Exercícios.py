"""
Exercícios:

1 - Faturamento do melhor e do pior mês do ano.
 Qual foi o valor de vendas do melhor mês do ano? E valor do pior mês do ano?

"""
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_total = vendas_1sem + vendas_2sem

melhor_mes = vendas_total.index(max(vendas_total))
melhor = meses[melhor_mes]

pior_mes = vendas_total.index(min(vendas_total))
pior = meses[pior_mes]

print(f'O melhor mês foi {melhor} com um total de vendas de {max(vendas_total)}.')
print(f'O pior mês foi {pior} com um total de vendas {min(vendas_total)}')


# 2 - Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

total = sum(vendas_total)
calc = (max(vendas_total) / total) * 100

print(f'O valor total é de R$ {total:,}. O número de vendas do melhor mês ({melhor}), representa {calc:.2f}% do valor total.')

# 3 - Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho").

while len(vendas_total) > 3:
    vendas_total.remove(min(vendas_total))

print(vendas_total)

# Forma alternativa
top3 = []
maior_valor = max(vendas_total)
top3.append(maior_valor)
vendas_total.remove(maior_valor)

maior_valor = max(vendas_total)
top3.append(maior_valor)
vendas_total.remove(maior_valor)

maior_valor = max(vendas_total)
top3.append(maior_valor)
vendas_total.remove(maior_valor)

top3.sort()
print(top3)


