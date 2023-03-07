"""
Exercícios

Para fazer um treino simples antes de avançarmos em mais functions, vamos criar uma function que resolve 1 'desafio simples'

Function para cálculo de carga tributária

(lembrando, não se atente ao funcionamento real da carga tritbutária, é apenas um exemplo imaginário para treinarmos as functions
 com algo mais prático)

Imagine que você trabalha no setor contábil de uma grande empresa de varejo

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os
custos (com exceção d o imposto) dele.

"""

preco = 1500
custo = 400
lucro = 800

def cal_tribut(preco, custo, lucro):
    imposto = preco - custo - lucro
    carga = imposto / preco
    return carga

print(f"A carga tributária foi de: {cal_tribut(preco, custo, lucro):.1%}")