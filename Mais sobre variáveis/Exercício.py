
#1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.

print("Olá mundo!")
print()

#============================================================
# 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

num = input("Informe um número: ")
print(f"O número informado foi: {num}")
print()

#============================================================
# 3. Faça um Programa que peça dois números e imprima a soma.

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
print(f"{num1} + {num2} é igual a {num1 + num2}.")
print()

#============================================================
# 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
print(f"A média das notas fornecidas é: {nota1 + nota2 + nota3 + nota4/4}. ")
print()

#============================================================
# 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

metro = float(input("Informe a metragem: "))
print(f"{metro} metro(s) é equivalente à {metro * 100:.2f} centímetros.")
print()

#============================================================
# 7. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

largura = float(input("Informe a largura: "))
altura = float(input("Informe a altura: "))
print(f"A área corresponde a {largura * altura:.2f} metros²")
print()

#============================================================
# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = int(input("Informe quantas horas você trabalha por mês: "))
valor = float(input("Informe quanto ganha por hora: "))
print(f"O seu salário é de R$ {horas * valor:.2f}")
print()

#============================================================
# 9. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. $C = \frac{5}{9}(F-32)$

temperatura = float(input("Informe a temperatura em Fahrenheit: "))

print(f"Essa é a temperatura convertida em Celsius {(temperatura - 32)/1.8:.2f} ")
print()

#============================================================
# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.$F = \frac{9}{5}C + 32$

temp = float(input("Informe a temperatura em celsius: "))
print(f"A temperatura correspodente em fahrenheit é {temp * 1.8 + 32:.2f} ")
print()

#============================================================
# 12. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:P = 72,7h - 58

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura(1.8 = 1 metro e 80 centímetros): "))
print(f"O seu IMC é correspondente a {peso/altura**2:.2f}\n")
print(f"O seu peso ideal é de {(72.7 * altura) - 58:.2f} Kg")
print()

#============================================================
# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: P = 72,7h - 58
# b. Para mulheres: P = 62,1h - 44,7

sexo = str(input("Informe seu sexo (masculino/feminino): ")).lower()
altura = float(input("Insira sua altura em metros: "))
peso = float(input("Insira seu peso em quilos: "))

if sexo == "feminino":
    print(f"O seu IMC é de {peso/altura**2:.2f}.")
    print(f"O seu peso ideal é de {(62.1 * altura) - 44.7:.2f} Kg\n")
else:
    print(f"O seu IMC é de {peso/altura**2:.2f}")
    print(f"O seu peso ideal é de {(72.7 * altura) - 58:.2f} Kg")

#============================================================
# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

ValorPHora = float(input("Informe quanto você ganha por hora trabalhada: "))

HoraMes = float(input("Informe qunatas horas por mês você trabalha: "))
print()
#####  Calcule o salário bruto (horas * salario por hora)

Sbruto = ValorPHora * HoraMes
print(f"De acordo com as informações fornecidas, seu salário bruto corresponde a R$ {Sbruto:.2f}")
print()

##### Calcule o desconto do IR (11% do salário bruto)
SalarioCDesc = Sbruto * 11/100
print(f"Com o desconto de 11% do IR, o valor será de R$ {Sbruto - SalarioCDesc:.2f}")
print()

##### Calcule o desconto do INSS (8% do salário bruto)
SalarioCDesc1 = Sbruto * 8/100
print(f"Com o desconto de 8% do INSS, o valor será de R$ {Sbruto - SalarioCDesc1:.2f}")
print()

##### Calcule o desconto do sindicato (5% do salário bruto)
SalarioCDesc2 = Sbruto * 5/100
print(f"Com o desconto do sindicato, o valor do será de R$ {Sbruto - SalarioCDesc2:.2f}")
print()

##### Calcule o salário líquido (salário bruto - descontos)
SalarioCDesc3 = Sbruto * 24/100
print(f"O valor líquido do salário é de R$ {Sbruto - SalarioCDesc3:.2f}")
print()

#============================================================
# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)

tamanho = int(input("Informe o tamanho da área a ser pintada em metros²: "))
litros = tamanho / 3
print(f"Para a área fornecida, serão necessários {round((litros/18)+0.5):.2f} latas.")

valor = litros/18
if valor == round(valor):
    print(f"O valor da compra será de R${valor * 80}")
else:
    print(f"O valor da compra será de R${round(valor+0.5) * 80:.2f}")


#============================================================
# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

TamArquivo = int(input("Informe o tamanho do arquivo: "))
VelDownload = int(input("Informe a velocidade de download em Megabits por segundo: "))

calc = TamArquivo / 0.125
tempo = calc / VelDownload

print(f"O download será concluído em {tempo / 60:.1f} minutos.")