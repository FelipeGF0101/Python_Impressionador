"""
ALTERAÇÕES INCREMENTAIS DE VARIÁVEIS

Estrutura:
* variavel = variavel + outro_valor

ou então

* variavel += outro_valor


"""
# Exemplo: Vamos adicionar às variáveis criadas, o produto ipad, 500 vendas.
lista = ['mac', 'iphone']
vendas = [100, 200]
# Adicionar ipad na lista

# lista.append('ipad')
# print(lista)

lista = lista + ['ipad']
print(lista)
print()

soma_vendas = 300
# adicionando na soma a quantidade de Ipad
soma_vendas = soma_vendas + 500
# Poderia ser: soma_vendas += 500 
print(soma_vendas)
print()

# Adicionando no fim do texto o Ipad
email = f"Esse mês vendemos um total de {soma_vendas} produtos, sendo:\n{vendas[0]} unidades de {lista[0]}\n{vendas[1]} unidades de {lista[1]}"
email = email + f'\n{500} unidades de Ipad'
print(email)