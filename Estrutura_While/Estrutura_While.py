"""
Funcionamento:
Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornoar verdadeira/falsa
A lógica é: enquanto a condição for verdadeira, o while executa o código. Assim que ela terminar de ser verdadeira, o código "sai" do while.

while condição:
    repete esse código

"""
# Exemplos: Quando criamos automações na internet
# Exemplos2: Crie um programa que funcione como o registro de vendas de uma empresa

# Nele, a pessoa deve inserir o nome do produto e o produto deve ser adicionado na lista de vendas. Enquanto o usuário não encerrar o programa,
# significa que ele está registrando novos produtos, então o programa deve permitir a entrada de quantos produtos o usuário quiser.

venda = input("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ")
vendas = []
#crie aqui o programa
while venda != '':
    vendas.append(venda)
    venda = input("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ")
    
print(f'Registro Finalizado. Os produtos cadastrados foram: {vendas}')