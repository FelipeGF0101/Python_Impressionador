"""
Exemplo prático

Digamos que você trabalha na Amazon (que tem centenas de milhares, se não milhões de produtos) e está analisando o resultado de vendas dos produtos.

Você precisa criar um programa que vai analisar o resultado de vendas dos produtos da Amazon em um mês. para simplificar vamos pensar em um único produto: iphone.

meta de vendas do iphone = 50.000 unidades
quantidade vendida no mês = 65.300 unidades

O seu programa deve avisar ( usaremos o print por enquanto) caso o produto tenha batido a meta do mês. Então devemos fazer: 

* Caso o produto tenha batido a meta, devemos exibir a mensagem: " Batemos a meta de vendas do Iphone, vendemos {} unidades"

* Se ele não bateu a meta do mês, o seu programa não deve fazer nada.

"""

meta = 50000
qtde_vendida = 65300

if qtde_vendida >= meta:
    print(f'Batemos a meta de vendas de Iphone, vendemos {qtde_vendida} unidades.')

"""
Tratando a condição falsa

Quando usamos o if, nem sempre queremos apenas analisar o caso verdadeiro, em boa parte das vezes, queremos fazer alguma coisa caso a condição seja verdadeira e fazer outra coisa caso a condição seja falsa.

Voltando ao nosso Exemplo real da Amazon e do Iphone, agora nosso programa deve avisar nos 2 casos:
* Caso o produto tenha batido a meta, devemos exibir a mensagem: " Batemos a meta de vendas de Iphone, vendemos {x} unidades

* Se ele não bateu a meta do mês, devemos exibir a mensagem: " Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades.

"""
meta = 50000
qtde_vendida = 65300

if qtde_vendida >= meta:
    print(f"Batemos a meta de vendas de Iphone, vendemos {qtde_vendida} unidades.")
else:
    print(f"Infelizmente não batemos a meta, vendemos {qtde_vendida} unidades. A meta era de {meta} unidades.")