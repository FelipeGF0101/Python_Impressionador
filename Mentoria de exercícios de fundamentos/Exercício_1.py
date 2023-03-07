"""
Imposto a pagar no lucro presumido

* 5% sobre faturamento de ISS (mensais)
* 0,65% de PIS sobre faturamento (mensal)
* 3% de COFINS sobre faturamento (mensal)
* 4.8% de IR (trimestral)
* 10% de IR adicional sobre o que ultrapassar 20 mil do faturamento (trimestral)
* CSLL 2,88% sobre faturamento (trimestral)

# percorrer cada item (mês) do dicionario
# para cada mês eu vou:
# vou transformar o valor em número
# calcular o imposto mensal
# calcular o imposto trimestral
# construir o resultado

"""
faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}


def transformando_valor(valor):
    valor = valor.replace("R$ ", "")
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")
    valor = float(valor)
    return valor

def calc_imposto_mensal(valor):
    iss = 0.05 * valor
    piss = 0.0065 * valor
    cofins = 0.03 * valor
    imposto_mensal = iss + piss + cofins
    return imposto_mensal

def calc_imposto_trimestral(valor):
    ir = 0.048 * valor
    csll = 0.0288 * valor
    if valor > 20000:
        ir_adicional = (valor - 20000) * 0.1
    else:
        ir_adicional = 0
    imposto_trimestral = ir_adicional + ir + csll
    return imposto_trimestral

for chave in faturamento:
    valor = transformando_valor(faturamento[chave])
    imposto_mensal = calc_imposto_mensal(valor)
    imposto_trimestral = calc_imposto_trimestral(valor)

    faturamento[chave] = (f'R$ {valor:.2f}, Mensal R$ {imposto_mensal:.2f}, Trimestral R$ {imposto_trimestral:.2f}')

for item in faturamento:
    print(item, faturamento[item])

"""
EXERCÍCIO 2

"""