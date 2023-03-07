"""
MAIS SOBRE O RETURN

Pontos importantes:

* Podemos usar no return praticamente qualquer tipo de objeto:(número, string, lista, tupla, dicionário, outros objetos, etc)
* O return, se for executado, encerra a função, mesmo que dentro dela haja um loop.

"""
# Retornar um número
def minha_soma(num1, num2, num3):
    return num1 + num2 + num3

meu_calc = minha_soma(10, 20, 30)
print(meu_calc)
print()

# Retornar um texto
def padronizar_texto(texto):
    texto = texto.lower()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

text = padronizar_texto('  FeLIPe    ')
print(text)
print()

# Retornar um boolean
def bateu_meta(vendas, meta):
    if vendas >= meta:
        return True
    else:
        return False

vendas = bateu_meta(300, 500)
print(vendas)
print()

# Retornar uma lista, tupla ou dicionario
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada

lista_textos = ['lira@gmail.com', 'zezinho@hotmail', 'joao@gmail.com', 'alon@gmail.com']
lista = filtrar_lista_texto(lista_textos,'gmail')
print(lista)
