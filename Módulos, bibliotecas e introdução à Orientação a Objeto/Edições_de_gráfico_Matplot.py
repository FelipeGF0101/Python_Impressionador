"""
Mais edições de gráfico com Matplot Lib

"""
# importando o matplotlib
import matplotlib.pyplot as plt

# Usando o módulo numpy para trabalhar com números

# Importando o módulo numpy

import numpy as np

# OUTROS TIPOS DE GRÁFICO:

# Linha

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.plot(meses, vendas, color='red')
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()

# Editando gráfico de linha

# Dispersão

# plt.scatter(meses, vendas)
# plt.show()

# Barra

plt.bar(meses, vendas, color="green")
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()

# Trabalhando com múltiplos gráficos no mesmo "plot" -> Para melhor visualização/comparação

plt.figure(1, figsize=(15, 3))
plt.subplot(2, 2, 1)
plt.plot(meses, vendas, color='red')

plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)

plt.subplot(1, 3, 3)
plt.bar(meses, vendas, color="green")
plt.show()