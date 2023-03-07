"""
Criando um mini sistema de controle de estoque

* Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição

*Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivemos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print)para fazer um novo pedido daquele produto.

* Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:
-> alimentos : Estoque mínimo: 50
-> bebidas : Estoque mínimo: 75
-> limpeza : Estoque mínimo: 30

Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem. Agora se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

Obs: Lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.
Obs1: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.

"""

nome = input("Informe o nome do produto: ")
quantidade = int(input("Infome a quantidade atual do produto: "))
categoria = input("Informe a categoria do protuto (alimento, bebida, limpeza): ")

if nome and quantidade and categoria:
    if categoria == "bebida":
        if quantidade < 75:
            print(f"Estoque baixo! Solicitar {nome} à equipe de compras. Temos apenas {quantidade} em estoque.")
    if categoria == "alimento":
        if quantidade < 50:
            print(f"Estoque baixo! Solicitar {nome} à equipe de compras. Temos apenas {quantidade} em estoque.")
    if categoria == "limpeza":
        if quantidade < 30:
            print(f"Estoque baixo! Solicitar {nome} à equipe de compras. Temos apenas {quantidade} em estoque.")
else:
    print("Preencha as informações corretamente.")

