"""
Comparadores

== -- igual
!= -- diferente
> -- maior que
< -- menor que
>= -- maior ou igual
<= -- menor ou igual
in -- o texto existe dentro de outro texto
not -- verifica o contrário da comparação

"""
# Teste

faturamento_loja_1 = 2500
faturamento_loja_2 = 2200
email = "felipe@gmail.com"

print("Programa 1")
if faturamento_loja_1 == faturamento_loja_2:
    print("Os faturamentos são iguais")
else:
    print("Os faturamentos são diferentes")
print()

print("Programa 2")
if email != "felipe@gmail.com":
    print("Esse não é o email do Felipe")
else:
    print("Email errado")
print()

print("Programa 3")
email_usuario = input("Insira seu email: ")
if not '@' in email_usuario:
    print("Email inválido")
else:
    print("Email válido")

# Também tenho a opção colocar um 'pass' caso não queira executar nada dentro do bloco do if. else:
#          pass

