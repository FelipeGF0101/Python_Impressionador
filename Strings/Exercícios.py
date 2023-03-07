"""
Cadastro de CPF

Crie um programa para cadatro de CPF de clientes que recebe o CPF em um input box apenas com números.
EX: Insira seu cpf (digite apenas números)

Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do cpf brasileiro), o programa deve exibir uma mensagem de:
"Digite seu cpf corretamente e digite apenas números."

cpf = input("Insira seu CPF (digite apenas números): ")
if (cpf.isnumeric()) == True and (len(cpf) == 11):
    print(f"Seu cpf é: {cpf}")

else: 
    print("Digite seu cpf corretamente e digite apenas números")
"""

"""
MELHORANDO NOSSO CADASTRO DE CPF

Agora, além das validações anteriores, vamos criar um input que permite que o usuário insira pontos, traços e inclusive espaços vazios.
Nosso programa deve "tratar" o que o usuário inserir para padronizar o cpf dele em apenas números.

A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços vazios
que o cliente inserir, e um vez retidados os pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF já só com número.
cpf1 = input("Insira seu CPF: ").replace('.', '').replace('-', '').strip()
if (cpf1.isnumeric()) == True and (len(cpf1) == 11):
    print(f"Seu cpf é: {cpf1}")
else:
    print("CPF INVÁLIDO! Insira um cpf válido!")
"""

"""
CADASTRO DE E-MAILs

* A hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido,
verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:

- felipegmail.com NÃO é um e-mail válido
- felipe@gmail NÃO é um e-mail válido
- felipe@gmail.com É  um e-mail válido

Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verificque:
1. Se o nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente.

2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido.

"""
nome = input('Insira seu nome: ').title()
verificanome = nome.replace(' ', '')
email = input('Insira seu e-mail: ').strip()
verifica = email.split('@')

if (verificanome.isalpha()) == True:
    if (verifica[0].isalpha()) == True or (verifica[0].isalnum()) == True:
        if (verifica[1].endswith('gmail.com')) == True:
            print(f'Nome: {nome:^30}| E-mail: {email:^30}')
else:
    print("Preencha os campos da forma correta!")


'''
RESPOSTA ALTERNATIVA 

nome1 = input('Digite seu nome: ')
email = input('Digite seu email: ')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluído')
    else:
        print('Email inválido')
else:
    print('Digite seu nome e e-mail corretamente')
'''