"""
Exibindo Gráficos no Python

Importância:
Para exploração e visualização de dados, nada melhor do que usar gráficos para isso. Apesas do Python ser programação, gráficos facilitam d+ em qulaquer 
projeto que trabalhe com dados.

Estrututa:
Usaremos o módulo Matplotlib, pyplot que é o módulo mais usado no python. Existem outros, como Seaborn e o plotly, caso queira ver/uar


"""

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

# Plotar gráfico da forma mais simples

import matplotlib.pyplot as plt

#plt.plot(vendas_meses)
#plt.show()

# Adicionar um Label no eixo X ou eixo Y

plt.plot(meses, vendas_meses) # É possível usar duas listas como parâmetro. Uma pro eixo X e outra pro Y
#plt.plot(eixo X, eixo Y)
plt.ylabel('Y Vendas')
plt.xlabel('X Meses')
plt.axis([0, 12, 0, max(vendas_meses)]) # É possível usar assim tbm plt.axis([0, 12, 0, 3000])
# plt.axis([valor mínimo do eixo x, valor máximo do eixo x, valor mínimo do eixo Y e valor máximo do eixo Y])
plt.show() # Isso deve ficar depois de qualquer alteração no gráfico