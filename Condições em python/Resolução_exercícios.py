"""
# 1. Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if num1 > num2:
    print(f"O maior número é o {num1}")
else:
    print(f"O maior número é o {num2}")

# ==============================================================

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Insira um valor: "))
if valor > 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")

# ==============================================================

# 3. Faça um Programa que verifique o estado civil de uma pessoa. 
# Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros).
# Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil, exemplo:

# Usuário digita: C
# Seu programa deve responder:
# C - Casado

nome = input("Insira seu nome: ")
estadoCivil = input("Insira seu estado civil (C: Casado, S: Solteiro, D: Divorciado, V: Viúvo, O: Outros): ").upper()

if estadoCivil == "C":
    print(f"{nome} é casado(a)." )

elif estadoCivil == "S":
    print(f"{nome} é solteiro(a).")

elif estadoCivil == "D":
    print(f"{nome} é divorciado(a).")

elif estadoCivil == "V":
    print(f"{nome} é viúvo(a).")

elif estadoCivil == "O":
    print(f"{nome} escolheu a opção Outros.")

else:
    print(f"{nome}, escolha uma das opções válidas.")

# ==============================================================

# 4. Faça um Programa que verifique se o e-mail digitado faz parte dos e-mails de spam.
# emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"

emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"

email = input("Insira seu email: ")
if email in emails_spam:
    print("Este email está classificado como spam.")
else:
    print("Este email é válido!")

# ==============================================================

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2)/2

if media >= 7 and media < 10:
    print("Aluno aprovado!")
elif media == 10:
    print("Aluno aprovado com distinção!")
else:
    print("Aluno reprovado!")

# ==============================================================

# 6. Faça um Programa que leia o orçamento de 3 empresas e mostre o maior deles.

emp1 = float(input("Insira o orçamento da empresa 1: "))
emp2 = float(input("Insira o orçamento da empresa 2: "))
emp3 = float(input("Insira o orçamento da empresa 3: "))

if emp1 > emp2 and emp1 > emp3:
    print("A empresa 1 tem o maior orçamento!")
elif emp2 > emp1 and emp2 > emp3:
    print("A empresa 2 tem o maior orçamento!")
else:
    print("A empresa 3 tem o maior orçamento!")

# ==============================================================

# 7. Faça um Programa que leia três orçamentos e mostre o maior e o menor deles.

emp1 = float(input("Insira o orçamento da empresa 1: "))
emp2 = float(input("Insira o orçamento da empresa 2: "))
emp3 = float(input("Insira o orçamento da empresa 3: "))

if emp1 > emp2 and emp1 > emp3:
    print("A empresa 1 tem o MAIOR orçamento!")
    
elif emp2 > emp1 and emp2 > emp3:
    print("A empresa 2 tem o MAIOR orçamento!")

else:
    print("A empresa 3 tem o MAIOR orçamento!")

if emp1 < emp2 and emp1 < emp3:
    print("A empresa 1 tem o MENOR orçamento!")

elif emp2 < emp1 and emp2 < emp3:
    print("A empresa 2 tem o MENOR orçamento!")

else:
    print("A empresa 3 tem o MENOR orçamento!")

# ==============================================================

# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Informe o valor do primeiro produto: "))
produto2 = float(input("Informe o valor do segundo produto: "))
produto3 = float(input("Informe o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve levar o produto 1.")
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve levar o produto 2.")
else:
    print("Você deve levar o produto 3.")

# ==============================================================

# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.


num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"{num1}, {num2}, {num3}")

elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"{num2}, {num1}, {num3}")

elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f"{num3}, {num2}, {num1}")

elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f"{num1}, {num3}, {num2}")

elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f"{num2}, {num3}, {num1}")

elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f"{num3}, {num1}, {num2}")

print()
# Resolução alternativa

if num1 > num2 and num1 > num3:
    print(f"O maior número é o {num1}")
    if num2 > num3:
        print(f"O segundo maior número é o {num2}")
        print(f"O terceiro maior número é o {num3}")
    else:
        print(f"O segundo maior número é o {num3}")
        print(f"O terceiro maior número é o {num2}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é o {num2}")
    if num1 > num3:
        print(f"O segundo maior número é o {num1}")
        print(f"O terceiro maior número é o {num3}")
    else:
        print(f"O segundo maior número é o {num3}")
        print(f"O terceiro mairo número é o {num1}") 
elif num3 > num1 and num3 > num2:
    print(f"O maior número é o {num3}")
    if num1 > num2:
        print(f"O segundo maior número é o {num1}")
        print(f"O terceiro maior número é o {num2}")
    else:
        print(f"O segundo maior número é o {num2}")
        print(f"O terceiro maior número é o {num1}")

# ==============================================================

# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Informe o turno que você estuda (M, V, N): ").upper()
if turno == "M":
    print("Bom dia")
elif turno == "V":
    print("Boa tarde")
elif turno == "N":
    print("Boa noite")
else:
    print("Valor inválido")

# ==============================================================

# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe
#  o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R\\$ 280,00 (incluindo) : aumento de 20% 

# salários entre R\\$ 280,00 e R\\$ 700,00 : aumento de 15% 

# salários entre R\\$ 700,00 e R\\$ 1500,00 : aumento de 10% 

# salários de R\\$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: 

# o salário antes do reajuste;

# o percentual de aumento aplicado;

# o valor do aumento;

# o novo salário, após o aumento.

# Obs: Não vamos nos preocupar tanto com a formatação dos números (nº de casas decimais, por exemplo, veremos isso no próximo módulo)

nome = input("Informe seu nome: ")
salario = float(input("Informe seu salário: "))

if salario <= 280:
    acrescimo = salario + salario * 0.20
    print(f"{nome}, você obteve um aumento de 20%, que equivale a R$ {salario * 0.20:.2f}. O seu salário passou de R$ {salario:.2f} para R$ {acrescimo:.2f}.")

elif salario > 280 and salario <= 700:
    acrescimo = salario + salario * 0.15
    print(f"{nome}, você obteve um aumento de 15%, que equivale a R$ {salario * 0.15:.2f}. O seu salário passou de R$ {salario:.2f} para R$ {acrescimo:.2f}.")

elif salario > 700 and salario <= 1500:
    acrescimo = salario + salario * 0.10
    print(f"{nome}, você obteve um aumento de 10%, que equivale a R$ {salario * 0.10:.2f}. O seu salário passou de R$ {salario:.2f} para R$ {acrescimo:.2f}.")

elif salario > 1500:
    acrescimo = salario + salario * 0.05
    print(f"{nome}, você obteve um aumento de 5%, que equivale a R$ {salario * 0.05:.2f}. O seu salário passou de R$ {salario:.2f} para R$ {acrescimo:.2f}.")

# ==============================================================

# 12 . Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
#  e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#  O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00


valorHora = float(input("Informe o valor da sua hora de trabalho: "))
horasTrab = int(input("Informe quantas horas trabalhadas no mês: "))
bruto = valorHora * horasTrab
print()
print(f"Seu salário bruto é de R$ {bruto:.2f}")
print()

if bruto <= 900:
    print(f"Salários de até R$ 900 estão isentos do IR.")
    print(f"Desconto do INSS (10%): R$ {bruto * 0.10:.2f}")
    print(f"Desconto do FGTS (11%): R$ {bruto * 0.11:.2f}")
    print(f"O total de descontos é de R$ {bruto * 0.10:.2f}")
    print(f"O salário líquido corresponde a R$ {bruto - bruto * 0.10:.2f}")
elif bruto > 900 and bruto <= 1500:
    print(f"Salários acima de R$ 900 e abaixo de R$ 1500 devem pagar IR.")
    print(f"Desconto do IR (5%): R$ {bruto * 0.05:.2f}")
    print(f"Desconto do INSS (10%): R$ {bruto * 0.10:.2f}")
    print(f"Desconto do FGTS (11%): R$ {bruto * 0.11:.2f}")
    print(f"O total de descontos é de R$ {bruto * 0.05 + bruto * 0.10:.2f}")
    print(f"O salário líquido corresponde a R$ {bruto - (bruto * 0.05 + bruto * 0.10):.2f}")
elif bruto > 1500 and bruto <= 2500:
    print(f"Salários acima de R$ 1500 e abaixo de R$ 2500 devem pagar IR.")
    print(f"Desconto do IR (10%): R$ {bruto * 0.10:.2f}")
    print(f"Desconto do INSS (10%): R$ {bruto * 0.10:.2f}")
    print(f"Desconto do FGTS (11%): R$ {bruto * 0.11:.2f}")
    print(f"O total de descontos é de R$ {bruto * 0.10 + bruto * 0.10:.2f}")
    print(f"O salário líquido corresponde a R$ {bruto - (bruto * 0.10 + bruto * 0.10):.2f}")
else:
    print(f"Salários acima de R$ 2500 devem pagar IR.")
    print(f"Desconto do IR (20%): R$ {bruto * 0.20:.2f}")
    print(f"Desconto do INSS (10%): R$ {bruto * 0.10:.2f}")
    print(f"Desconto do FGTS (11%): R$ {bruto * 0.11:.2f}")
    print(f"O total de descontos é de R$ {bruto * 0.20 + bruto * 0.10:.2f}")
    print(f"O salário líquido corresponde a R$ {bruto - (bruto * 0.20 + bruto * 0.10):.2f}")

# ==============================================================

# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Escolha um número de 1 a 7: "))
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Terça")
elif numero == 4:
    print("Quarta")
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta")
elif numero == 7:
    print("Sábado")
else:
    print("Insira um valor válido!")

# ==============================================================

# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Em seguida, mostre qual conceito o aluno teve. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2)/2
print(media)

print()
if media >= 9.0 and media <= 10.0:
    print("Você tirou um A")
elif media > 7.5 and media < 9.0: 
    print("Você tirou um B")
elif media > 6.0 and media < 7.5:
    print("Você tirou um C")
elif media > 4.0 and media < 6.0:
    print("Você tirou um D")
else:
    print("Você tirou um E")

# ==============================================================

# 15. Você está construindo um calendário para controlar dias de trabalho a pedido do RH. Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, para montar o calendário de forma correta.
# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

Dica para determinar se um ano é bissexto: 
- São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
- São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, 
p.ex.: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028...
- Não são bissextos todos os demais anos.
ex1: 2004 é múltiplo de 4, mas não é múltiplo de 100, então é bissexto.
ex2: 2000 é múltiplo de 4, mas é múltiplo de 100, só que também é multiplo de 400, então é bissexto (porque todo ano múltiplo de 400 é bissexto, independente do resto).
ex3: 1900 é múltiplo de 4, é múltiplo de 100, mas não é múltiplo de 400, então não é bissexto


Dica: lembre que: numero % 4 é o resto da divisão do número por 4, ex: 10 % 3 = 1 (já que 10/3 = 3 e resta 1)

ano = int(input("Informe um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")

# ==============================================================

# 16. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7 and media < 10:
    print(f"O aluno foi aprovado com média {media:.2f}")
elif media < 7:
    print(f"O aluno foi reprovado com média {media:.2f}")
elif media == 10:
    print(f"Parabéns! Você foi aprovado com distinção.Sua média foi {media:.2f}")

# ==============================================================

# 17. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

limite = 50
peso = float(input("Insira o peso da sua pesca de hoje: "))

if peso > 50:
    excedente = peso - limite
    print(f"Você pegou mais do que o permitido. Você pegou o excedente de {excedente} quilos. Cada quilo excedente custa R$ 4.00. Nesse caso você irá pegar R$ {excedente * 4}")
else:
    print("Tudo certo!")

# ==============================================================

# 18. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.
Dica2: numero % 10 vai te dar o resto da divisão do número por 10.

valor = int(input("Informe o valor a ser sacado: "))

n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1 = 0

if 10 <= valor <= 600:
    print("São necessárias: ")
    if valor > 100:
        n100 = valor // 100
        print(f"{n100} notas de 100.")
    if valor % 100 >= 50:
        n50 = (valor - 100 * n100) // 50
        print(f"{n50} notas de 50.")
    if valor % 50 >= 10:
        n10 = (valor -100 * n100 - 50 * n50) // 10
        print(f"{n10} notas de 10.")
    if valor % 10 >= 5:
        n5 = (valor - 100 * n100 - 50 * n50 - 10 * n10) // 5
        print(f"{n5}, notas de 5.")
    if valor % 5 >= 1:
        n1 = valor - 100 * n100 - 50 * n50 - 10 * n10 - 5 * n5
        print(f"{n1} notas de 1.")
else:
    print("Informe um valor entre 10 e 600")

# ==============================================================

# 19. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

cont = 0
print("A cada questão apresentada, responde com S(sim) ou N(não)!")
p1 = input("Você telefonou para a vítma? ").upper()
if p1 == "S":
    cont += 1
p2 = input("Você esteve no local do crime? ").upper()
if p2 == "S":
    cont += 1
p3 = input("Você mora perto da vítma? ").upper()
if p3 == "S":
    cont += 1
p4 = input("Você devia para a vítma? ").upper()
if p4 == "S":
    cont += 1
p5 = input("Você já trabalhou com a vítma? ").upper()
if p5 == "S":
    cont += 1

if  cont == 2:
    print("Você se classifica como suspeito!")
elif cont >= 3 and cont <= 4:
    print("Você se classifica como cúmplice!")
elif cont == 5:
    print("Você é o assassino!")

# ==============================================================

# 20. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Informe o combustível que deseja (A - álcool, G - Gasolina): ").upper()
quant = float(input("Informe quantos litros deseja comprar: "))

if combustivel == "A":
    valor = quant * 1.90
    print(f"Valor normal: {valor:.2f}")
    if quant <= 20:
        print(f"Você escolheu Álcool. O valor a ser pago será de (valor com desconto) R$ {valor - valor * 0.03:.2f}.")
    elif quant > 20:
        print(f"Você escolheu Álcool. O valor a ser pago será de (valor com desconto) R$ {valor - valor * 0.05:.2f}.")
    
elif combustivel == "G":
    valor = quant * 2.50
    print(f"Valor normal: {valor:.2f}")
    if quant <= 20:
        print(f"Você escolheu Gasolina. O valor a ser pago será de (valor com desconto) R$ {valor - valor * 0.04:.2f}.")
    elif quant > 20:
        print(f"Você escolheu Gasolina. O valor a ser pago será de (valor com desconto) R$ {valor - valor * 0.06:.2f}.")

else:
    print("Insira as informações corretas!")

# ==============================================================

# 21. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = int(input("Informe quantos quilos de Morango deseja levar: "))
maca = int(input("Informe quantos quilos de Maçã deseja levar: "))

if morango <= 5:
    valorm1 = morango * 2.50
if morango > 5:
    valorm1 = morango * 2.20
if maca <= 5:
    valorm2 = maca * 1.80
if maca > 5:
    valorm2 = maca * 1.50

valorfinal = valorm1 + valorm2

if valorfinal > 25:
    print(f"Você comprou {morango} quilos de morangos e {maca} quilos de maçã. Compras acima de R$ 25.00 reais, recebem um desconto especial de 10%. O valor total a ser pago será de R$ {valorfinal - valorfinal * 0.10:.2f}.")
else:
    print(f"Você comprou {morango} quilos de morangos e {maca} quilos de maçã. O valor final é de R$ {valorfinal:.2f}")

# ==============================================================

# 22. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


carne = input("Informe a carne desejada (File duplo, Alcatra ou Picanha): ").lower()
quilo = float(input("Informe quantos quilos deseja levar: "))

if carne == "file duplo":
    if quilo <= 5:
        valor = quilo * 4.90
    if quilo > 5:
        valor = quilo * 5.80

elif carne == "alcatra":
    if quilo <= 5:
        valor = quilo * 5.90
    if quilo > 5:
        valor = quilo * 6.80

elif carne == "picanha":
    if quilo <= 5:
        valor = quilo * 6.90
    if quilo > 5:
        valor = quilo * 7.80

print(f"O total da sua compra foi de R$ {valor:.2f}")

pagamento = input("Vai pagar com cartão comum, dinheiro ou cartão tabajara? ").lower()

if pagamento == "cartão tabajara":
    print(f"Já que você está utilizando o cartão da loja, receberá um desconto de 5% no valor total da compra. O valor com desconto é de R$ {valor - valor * 0.05:.2f}")
    print("Obrigado por comprar em nossa loja!")
else:
    print("Obrigado por comprar em nossa loja!")

"""
