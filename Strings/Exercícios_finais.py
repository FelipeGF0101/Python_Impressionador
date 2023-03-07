"""
EXERCÍCIOS FINAIS DO MÓDULO

# 1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

"""
texto1 = 'Ilha do medo'
texto2 = 'A Ilha do medo'

print(f'O texo1: "{texto1:^30}" apresenta {len(texto1)} caracteres!')
print(f'O texo1: "{texto2:^30}" apresenta {len(texto2)} caracteres!')

if len(texto1) == len(texto2):
    print('Os textos possuem o mesmo número de caracteres!')
else: 
    print('Os textos possuem tamanhos diferentes')

if texto1 == texto2:
    print('Os textos são iguais')
else:
    print('Os textos são diferentes')
print()
"""
# 2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija
# o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

"""
telefone = input('Insira um número de telefone: ').strip()
if '-' in telefone:
    telefone = telefone.replace('-', '')

if len(telefone) == 7 and telefone.startswith('3') == False:
    print('O telefone informado está incompleto! O 3 será inserido automáticamente.')
    telefone = '3' + telefone
    print(f"Telefone corrigido: {telefone}")
    print()
    print(f'Telefone corrigido com formatação: {telefone[:4]}-{telefone[4:]}.')
else:
    print('O telefone informado não está completo!')