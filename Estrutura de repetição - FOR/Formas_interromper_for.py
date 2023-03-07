"""
Formas de interromper um for

2 opções:
-break -> interrompe e finaliza o for
-continue -> interrompe e vai para o próximo item do for

"""

vendas = [100, 150, 1500, 2000, 120]

# caso 1: Se todas as vendas forem acima da meta, a loja ganha bônus:
meta = 110 
for i in vendas:
    if i < meta:
        print("A loja não ganha bônus")
        break
    print(i)


# caso 2: Exiba quem bateu a meta
vendedores = ['Jão', 'Júlia', 'Ana', 'José', 'Maria']
meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)
