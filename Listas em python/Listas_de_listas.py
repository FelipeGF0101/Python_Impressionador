"""
Listas de listas

Estrutura:

Cada item de uma lista pode ser qualquer tipo de variável. Inclusive, uma lista.

Quando dentro de uma lista temos cada item como sendo uma outra lista, temos uma "nested list",
ou seja, uma lista de listas.

Todas as regras de lista e tudo que vimos até agora funciona exatamente igual, mas vamos ver como
isso funciona na prática.

"""
vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['Ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10]
]

# Quanto joão vendeu de IPAD?
i_vendedores = vendedores.index('João')
i_produtos = produtos.index('Ipad')
vendas_joao = vendas[i_vendedores][i_produtos]
print(vendas_joao)
print()

# Quanto Diego vendeu de Iphone?
i_vendedores = vendedores.index('Diego')
i_produtos = produtos.index('iphone')
vendas_diego = vendas[i_vendedores][i_produtos]
print(vendas_diego)
print()

# Qual o total de vendas de Iphone?
vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print(vendas_iphone)
print()

# E se Lira na verdade fez apenas 50 vendas de Iphone, como eu modifico na minha lista o valor de vendas dele?
i_vendedores = vendedores.index('Lira')
i_produtos = produtos.index('iphone')
vendas[i_vendedores][i_produtos] = 50
vendas_Lira = vendas[i_vendedores][i_produtos]
print(vendas_Lira)
print()

# E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em casa um dos vendedores?
produtos.append('mac')
print(produtos)

vendas_mac = [10, 15, 6, 70]
vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])

print(vendas)
