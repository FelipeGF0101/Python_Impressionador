"""
Estrutura: 

tupla = (valor, valor, valor...)

Diferença 
Parece uma lista, mas é imutável.

vantagens:

* Mais eficiente (em termos de performance)
* Protege a base de dados (por ser imutável)
* Muito usado para dados heterogêneos

"""
# Criando Tuplas:

vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
print(vendas)

# Acessando valor de uma tupla:

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(nome, data_contratacao, data_nascimento, salario, cargo)
print()

# O enumerate que vinhamos usando até agora, na verdade, cria uma tupla para a gente. Vamos ver na prática:
vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['joão', 'Lira','Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):
    print(f'{funcionarios[i]} vendeu {venda} unidades.')
print()

# Unpacking de tupla é uma outra forma de acessar valores contidos em uma tupla. Por exemplo:
vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
nome, data_contratacao, data_nascimento, salario, cargo = vendas 
print(nome)

# Regras: o número de variáveis no unpacking deve ser exatamente proporcional ao número de valores dentro da tupla.
