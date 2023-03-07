"""
Módulo Time

Estrutura:

* Um dos módulos mais usado no Python. Tudo que diz respeito a data, a marcar quanto tempo leva alguma ação,
ou a tempo mesmo, o módulo time vai ajudar a gente.

"""

import time

# Marco Zero (chamado de EPOCH) = 1 de Janeiro de 1970 às 00:00:00
# time() retorna quantos segundos se passaram desde a EPOCH

segundos_hoje = time.time()
print(segundos_hoje)

# ctime retorna a data em string o texto no formato UTC  (um formato padrão de datas)

data_hoje = time.ctime()
# ou então data_hoje = time.ctime(time())
print(data_hoje)

# Isso já pode ser muito útil para medir o temp que uma ação leva, caso seja interesse:
tempo_inicial = time.time()
for i in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(f'O programa levou {duracao} segundos para rodar.')

# Fazer o código esperar alguns segundos (muito útil quando temos que esperar um programa ou uma página carregar)

# para esperar 5 segundos fazemos:
print('começando')
time.sleep(5)
print('Rodou 5 segundos após')

# Pegar informações de dias, hora, segundo, minuto, tudo detalhado.
# gmtime()
# gmtime().parâmetro

data_atual = time.gmtime()
print(data_atual)
 # Resultado: time.struct_time(tm_year=2023, tm_mon=3, tm_mday=2, tm_hour=19, tm_min=38, tm_sec=42, tm_wday=3, tm_yday=61, tm_isdst=0)

# É um objeto diferente, mas podemos pegar os parâmetros de ano, mês, dia, etc... fazendo:

ano = data_atual.tm_year
mes = data_atual.tm_mon
dia = data_atual.tm_mday
hora = data_atual.tm_hour
dia_da_semana = data_atual.tm_wday
dias_passados_ano = data_atual.tm_yday
print(f'Hoje é: {dia}/{mes}/{ano} | hora: {hora} | dia da semana: {dia_da_semana} | já se passaram {dias_passados_ano} dias do ano de {ano}')