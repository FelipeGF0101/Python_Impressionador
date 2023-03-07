"""
Como descobrir o índice de um item de uma lista

i = lista.index('item')



# Exemplo:

# Digamos que você puxou do Banco de Dados da sua empresa uma lista com todos os produtos que a empresa vende e a quantidade em estoque de todos eles.

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

# Nesse caso a lista é 'pequena', para fins didáticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.
# E agora, como fazer para descobrir a quantidade em estoque do produto geladeira?

i = produtos.index('geladeira') # Busca o índice do produto
qtde_estoque = estoque[i] # Usa o índice para encontrar o valor na posição correspondente da outra lista

print(f'Quantidade em estoque da geladeira é de: {qtde_estoque}')
#===================================================================

i1 = produtos.index('tablet')
quantidade = estoque[i1]

print(quantidade)
print()
#===================================================================
"""
# Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista,
# ele deverá ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto.

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

produto = input('Insira o nome do produto: ')

if produto in produtos:
    i = produtos.index(produto)
    quantidade = estoque[i]
    print(f'O produto {produto.upper()} encontra-se em estoque com {quantidade} unidades!')
else:
    print(f'{produto.upper()} não existe no estoque!')