"""
Format - aula de consulta

Como usar o format para criar formatações personalizadas em prints e textos

:< - Alinha o texto à esquerda (se tiver espaço na tela para isso);
:> - Alinha o texto à direita (se tiver espaço na tela para isso);
:^ - Alinha o texto ao centro (se tiver espaço na tela para isso);
:+ - Coloca o sinal sempre na frente do número (independente se é positivo ou negativo);
:, - Coloca a vírgula como separador de milhar;
:_ - Coloca o _ como separador de milhar;
:e - Formato Científico;
:f - Número com quantidade fixa de casas decimais;
:x - Formato HEX minúscula (para cores);
:X - Formato HEX maiúscula (para cores);
:% - Formato percentual.
"""

# EXEMPLO DE ALINHAMENTO

email = 'felipe@gmail.com'
print(f'Meu email não é {email:<30}, certo?')
print(f'Meu email não é {email:>30}, certo?')
print(f'Meu email não é {email:^30}, certo?')
print()

# EXEMPLO DE EDIÇÃO DE SINAL
custo = 500
faturamento = 250
lucro = faturamento - custo
print(f'Faturamento foi {faturamento:+} e o lucro foi {lucro:+}')
print()

# EXEMPLO DE SEPARADOR DE MILHAR
custo1 = 5000
faturamento1 = 2500
lucro1 = faturamento1 - custo1
print(f'Faturamento foi {faturamento1:,} e o lucro foi {lucro1:,}')
# Também é possível usar a sinal junto com separador de milhar
print(f'Faturamento foi {faturamento1:+,} e o lucro foi {lucro1:+,}')
print()

# FORMATO COM CASAS DECIMAIS FIXAS
custo2 = 500
faturamento2 = 250
lucro2 = faturamento2 - custo2
print(f'Faturamento foi {faturamento2:.2f} e o lucro foi {lucro2:.2f}')
print()

# FORMATO PERCENTUAL
custo3 = 500
faturamento3 = 1300
lucro3 = faturamento3 - custo3
margem = lucro3 / faturamento3
print(f"A margem de lucro foi de {margem:.2%}.")
print()

# FORMATO MOEDA -> COMBINAÇÕES DE FORMATO
# Existem módulos/ bibliotecas que vão facilitar isso, caso a gente queira, mas vamos ver como usar módulos mais a frente do curso.
# Por enquanto, se você precisar, pode fazer substituíção em string.

custo4 = 5000
faturamento4 = 2500
lucro4 = faturamento4 - custo4
print(f'Faturamento foi R$ {faturamento4:,.2f} e lucro foi R$ {lucro4:,.2f}')

#transformando no formato brasileiro
lucro_texto = f'R$ {lucro4:_.2f}'
print(lucro_texto.replace('.', ',').replace('_','.'))
print()

# FUNÇÃO ROUND PARA ARREDONDAR NÚMEROS, CASO SEJA NECESSÁRIO

imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print(f'Imposto sobre o preço é de {valor_imposto}')