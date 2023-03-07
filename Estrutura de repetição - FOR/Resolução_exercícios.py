""" 
# 1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas. 
"""
vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

for i, venda in enumerate(vendas):
    print(f'Vendedor: {vendedores[i]} => Vendas: {venda}')
print(f'Média de vendas: {sum(vendas)/len(vendas):.2f}')
print()

"""
# 2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.
"""
alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

lista_final = []
cont = 0

for i, aluno in enumerate(alunos):
    qtde = len(notas[0])
    media = sum(notas[i])
    media_final = media / qtde
    nota = [f"Nome: {alunos[i]}", f"Média: {media_final}"]
    lista_final.append(nota)
    if media_final >= 7:
        cont += 1

for a in lista_final:
    print(a)

print(f'{cont} alunos tiveram nota acima de 7.')
print()

"""
# 3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com mais de 25 anos possuem salário inferior à média de todos os salários.

"""
idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]

media = sum(salarios) / len(salarios)
cont = 0
for i , idade in enumerate(idades):
    if idade > 25:
        if salarios[i] < media:
            cont += 1
            atribuicao = [f'Idade: {idade}', f"Salário: {salarios[i]}"]
            print(atribuicao)
print()
print(f"A média dos salários é R$ {media:.2f}".replace('.',','))        
print(f"{cont} funcionários possuem salário menor que a média!")
print()

"""
# 4.Em quais meses a média de temperatura foi maior do que a média nacional?
"""
meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]
lista_final = []

med_nacional = sum(temperaturas) / len(temperaturas)

for i, mes in enumerate(meses):
    if temperaturas[i] > round(med_nacional):
        lista = [f"Mes: {mes}", f"Temperatura: {temperaturas[i]}"]
        lista_final.append(lista)
print(lista_final)
print()

"""
# 5. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
O programa deverá calccular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""

lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
abonos = []
cont = 0
for salario in lista_salarios:
    calc = salario * (0.2 + 1) - salario
    if calc < 100:
        calc = 100
    abonos.append(calc)
    if calc == 100:
        cont += 1
    print(f"Salário: R$ {salario:.2f} - Abono:R$ {calc:.2f}")
    print()

print(f'Foram processados {len(lista_salarios)} colaboradores.')
print(f'Total gasto com abono: R$ {sum(abonos):.2f}')
print(f'Valor mínimo pago para {cont} colaboradores')
print(f'Maior valor de abono pago: R$ {max(abonos):.2f}')
print()

"""
# 6. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
Calcule e mostre:

a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. 
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.

"""
modelos = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeot']
autonomias = [7, 10, 12.5, 9, 14.5]

print('Relatório final:')
for i, autonomia in enumerate(autonomias):
    print(f' {i+1} - {modelos[i]} - {autonomia:.1f} - Consumo em uma distância de 1000km: {1000/autonomia:.2f} Litros - Custando: R$ {1000/autonomia* 2.25:.2f}')

maior = max(autonomias)
i = autonomias.index(maior)
print(f'O menor consumo é do {modelos[i]}')
print()

