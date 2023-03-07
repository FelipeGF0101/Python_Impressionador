"""
EXERCÍCIOS

1 - Calculando % de uma lista.

Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso,
mas com o nosso conhecimento atual, já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero 
conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.

"""
bateram_meta = []
meta = 10000
vendas = [
    ['joão', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3759],
    ['Ana', 10300],
    ['Alon', 7870]
]

for item in vendas:
    if item[1] >= meta:
        bateram_meta.append(item)
print(bateram_meta)

print(f"Apenas {len(bateram_meta)/len(vendas):.1%} bateram a meta!")

"""
Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?

"""
melhor = ''
maior = 0
for item in vendas:
    if item[1] > maior:
        maior = item[1]
        melhor = item[0]

print(f'O maior vendedor(a) foi {melhor} com {maior} vendas.')
                