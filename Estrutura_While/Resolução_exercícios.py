"""
# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    num = int(input('Informe um valor entre 0 e 10: '))
    if num < 0 or num > 10: 
        print("Insira um valor válido!")
    else:
        print('Obrigado!')
        

"""

"""
# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


nome = input("Insira seu nome: ")
senha = input("Insira sua senha: ")

while True:
    if nome == senha:
        print('PARA SUA SEGURANÇA, A SENHA NÃO PODE SER IGUAL AO NOME.POR FAVOR ESCOLHA OUTRA SENHA...')
    else:
        print('Tudo certo!')
        
    nome = input("Insira seu nome: ")
    senha = input("Insira sua senha: ")

# RESOLUÇÃO ALTERNATIVA

login = input('Informe o login: ')
senha = input('Informe o senha: ')
while login == senha:
    print('O login não pode ser igual à senha')
    login = input('Informe o login: ')
    senha = input('Informe o senha: ')

"""
"""
# 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = input('Informe seu nome: ').capitalize()
while len(nome) < 4:
    print('Nome inválido! Insira um nome válido.')
    nome = input('Informe seu nome: ').capitalize()

idade = int(input("Informe a idade: "))
while not (0 <= idade <= 150):
    print('Idade fornecida é inválida! Por favor forneça a idade correta.')
    idade = int(input("Informe a idade: "))

salario = float(input('Informe seu salário: '))
while salario <= 0:
    print('Valor inserido é inválido! Informe um valor correto.')
    salario = float(input('Informe seu salário: '))

sexo = input("Informe o seu sexo (f ou m): ")
while not sexo in ['m', 'f']:
    print('Informe o sexo corretamente. Escreva F para feminino ou M para masculino!')
    sexo = input("Informe o seu sexo (f ou m): ")

est_civil = input("Informe o estado civil: ")
while not est_civil in ['s', 'c', 'v', 'd']:
    print(f'Insira um estado civil válido')
    est_civil = input("Informe o estado civil: ")

"""

"""
# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.



a = 80000
b = 200000
cont = 0
while a < b:
    atualiza = a * 3 / 100
    a = a + atualiza
    atualiza_b = b * 1.5 / 100
    b = b + atualiza_b
    cont += 1  


print(f"Para que se igualem, A levará {cont} anos para chegar a populção de {a:,.2f}, tendo B a população de {b:,.2f} pessoas.")

"""

"""
# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


repete = 's'

while repete == 's':

    populacao_A = int(input('Informe a população A: '))
    populacao_B = int(input('Informe a população B: '))

    while populacao_A <= 0 or populacao_B <= 0:
        print('As populações precisam ser maiores que zero')
        populacao_A = int(input('Informe a população A: '))
        populacao_B = int(input('Informe a população B: '))

    taxa_A = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
    taxa_B = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))

    while taxa_A <= 0 or taxa_B <= 0:
        print('As taxas precisam ser maiores que zero')
        taxa_A = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
        taxa_B = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))

    taxa_A = taxa_A / 100 + 1
    taxa_B = taxa_B / 100 + 1

    tempo = 0

    while populacao_A < populacao_B:
        populacao_A *= taxa_A
        populacao_B *= taxa_B
        tempo += 1

    print('São necessários', tempo, 'anos para a população A igualar ou superar a população B')
    
    repete = input('Deseja repetir a operação? Tecle "s" para sim, qualquer outra tecla para não.')

"""

"""
# 6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento


for i in range(5):
    valor = float(input(f"Informe valor do faturamento do {i + 1}º mês: "))
    if i == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
print(f"O maior valor é : {maior}")

"""
"""
# 7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média).
soma = 0
cont = 0
for i in range(5):
    valor = float(input(f"Informe o valor do faturamento do {i + 1}º mês: "))
    soma += valor
    cont +=1

print(f"A soma de todos os valores é {soma:.2f} e a média de faturamento/mês é de {soma/cont:.2f}")

"""

"""
# 8. Faça um programa que consiga categorizar a idade das equipes de uma empresa. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da equipe 
varia entre 0 e 25 (jovem) ,26 e 60 (sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.

calc = 0
resp = 's'
cont_jovem = 0
cont_senior = 0
cont_idoso = 0

while resp == 's':
    idade = int(input("Informe a sua idade: "))
    calc += idade
    if idade > 0 and idade <= 25:
        cont_jovem += 1
    elif idade >= 26 and idade <= 60:
        cont_senior += 1
    else:
        cont_idoso += 1

    calc_total = cont_jovem + cont_senior + cont_idoso

    equipe = calc / calc_total
    if equipe > 0 and equipe <= 25:
        resultado = 'JOVEM'
    elif equipe >= 26 and equipe <= 60:
        resultado = 'SÊNIOR'
    else:
        resultado = 'IDOSA'

    resp = input("Deseja cadastrar mais alguém? (s, n)  ")

print(f"Na equipe, temos um total de {calc_total} pessoas. Sendo {cont_jovem} jovens, {cont_senior} seniores e {cont_idoso} idosos. Pela média das idades ({equipe}), esta equipe é considerada {resultado}")

"""

"""
# 9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

felipe = 0
pietro = 0
oliver = 0

eleitores = int(input("Informe o número de eleitores: "))

for i in range(eleitores):
    voto = int(input('Vote 1 para Felipe, vote 2 para Pietro, vote 3 para Oliver: '))
    while voto != 1 and voto != 2 and voto != 3:
        print('Opção inválida!')
        voto = int(input('Vote 1 para Felipe, vote 2 para Pietro, vote 3 para Oliver: '))

    if voto == 1:
        felipe += 1
    elif voto == 2:
        pietro += 1
    else:
        oliver += 1

print(f'Número de votos: Felipe = {felipe} | Pietro = {pietro} | Oliver = {oliver}')
"""

"""
# 11. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que
contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50

"""
print('Loja Quase Dois - Tabela de Preços: ')
for i in range(50):
    print(f'{i + 1} - R$ {(i + 1) * 1.99:.2f}')