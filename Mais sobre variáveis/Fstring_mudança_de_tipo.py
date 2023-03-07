""" F-String"""

faturamento = 1000
custo = 400

lucro = faturamento - custo

# Com format

print("O faturamento foi de {} e o lucro de {}".format(faturamento, lucro)) # A ordem importa

# Com f-string
print(f"O faturamento foi de {faturamento} e o lucro foi de {lucro}")
# O faturamento foi de 1000 e o lucro foi de 600

# Também poderia ser
print(f"O faturamento foi de {faturamento} e o lucro foi de {faturamento - custo}")
# O faturamento foi de 1000 e o lucro foi de 600

# =============================

# MUDANÇA DO TIPO DE VARIÁVEL

#faturamento = input("Insira o faturamento: ")
#custo = input("Insira o custo: ")
#lucro = faturamento - custo
#print(lucro)

# A operação acima irá gerar um erro de tipo. Da forma que o input foi feito acima, a informação é recebida como uma string e não como inteiro ou float. Para que o erro não ocorra é necessário informar o tipo de dado que o programa irá receber. Por exemplo: faturamento = int(input("Insira o faturamento: "))
# Não é possível realizar uma operação matemática entre duas strings
print()

# Forma correta
faturamento = int(input("Insira o faturamento: "))
custo = int(input("Insira o custo: "))

lucro = faturamento - custo

print(lucro)

# str -> muda para string
# int -> muda para inteiro
# float -> muda para float
