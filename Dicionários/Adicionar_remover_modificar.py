"""
ADICIONAR, REMOVER E MODIFICAR ITENS NO DICIONÁRIO

Estrutura:

* Adicionar itens:

dicionario = {}
dicionario[chave] = valor

outra opção:

dicionario.update({chave: valor, chave: valor})

"""
lucro_1tri = {'janeiro': 10000, 'fevereiro': 120000, 'marco': 90000}
lucro_2tri = {'abril': 88000, 'maio': 890000, 'junho':120000}

# adicionando 1 item
print(lucro_1tri)
lucro_1tri['abril'] = 88000
print(lucro_1tri)
print()

# adicionando vários itens ou um dicionário a outro
print(lucro_1tri)
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)
print()

# adicionando um item já existente (manualmente ou pelo update)
lucro_1tri['janeiro'] = 88000
print(lucro_1tri)
print()
# Dicionários não podem ter chaves repetidas. Quando tentamos colocar uma chave já existente no dicionário, o valor é apenas atualizado.

'''
# REMOVENDO ITENS:

del dicionario[chave]

ou então

valor = dicionario.pop(chave)

mas cuidado com:

del dicionario
-> que é diferente de dicionario.clear()

'''
# removendo o mês de junho

del lucro_1tri['junho']
print(lucro_1tri)
print()

# A diferença do del para o .pop() é que o pop armazena o valor em outra variável, o que não é o caso do del que apenas deleta o valor.
valor = lucro_1tri.pop('maio')
print(valor)
print(lucro_1tri)
print()
# O que acontece caso você não passe um parâmetro para o del
#del lucro_1tri
#print(lucro_1tri)

# O del simplismente deleta a variável. É como se ela não existisse mais a partir desse ponto

# utilizando o clear()
lucro_1tri.clear()
print(lucro_1tri)
# O clear limpa todo o dicionário, porém a variável ainda continua existindo

# OBS: o del também funciona para listas, caso queira usar
# del lista[i]
funcionarios = ['joão', 'lira', 'maria', 'ana', 'paula']
del funcionarios[0]
print(funcionarios)
