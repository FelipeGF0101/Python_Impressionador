"""
Casos com várias condições/comparações

Estrutura:
Quando temos várias comparações, ao invés de criar if dentro de if podemos usar os operadores "and" e "or" para tratar essas condições.

EXEMPLO

Vamos voltar ao exemplo de cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcionário e também com o resultado da empresa como um todo.

Nesse caso, a regra funciona da seguinte forma:

* Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas, o funcionário ganha 3% do que ele vendeu em bônus.

* Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um todo, o funcionário não ganha bônus.

"""
meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 280000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print(f'Bônus do funcionário foi de {bonus}')
else: 
    print("O funcionário não ganhou bônus!")
print()

"""
OUTRO EXEMPLO

Agora vamos levar essa análise mais a fundo.
Nessa empresa, existe um outro caso também que garante que o funcionário ganhe um bônus, independente das vendas que ele fez naquele mês. 

Todo mês od diretores da empresa fazem uma avaliação qualitativa de todos os funcionários. Nessa avaliação os diretores dão uma nota de 0 a 10 no funcionário. Se a nota do funcionário for 9 ou 10, ele também ganha o bônus de 3% do valor de vendas. (os bônus não são cumulativos)
"""
nota_funcionario = 9
meta_nota = 9

if nota_funcionario >= meta_nota or vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print(f"O bônus do funcionário foi de {bonus}")
else:
    print("O funcionário não ganhou bônus")