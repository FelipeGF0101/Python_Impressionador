"""
str -> Transforma número em string
in -> Verifica se um texto está contido dentro do outro
operador + -> concatenar string
format e {} -> substitui valores
%s -> Substitui textos 
%d -> Substitui números decimais

"""
faturamento = 1000
custo = 500
lucro = faturamento - custo
email = 'felipe@gmail.com'

# Uso do str() e do concatenar com +
# print("O faturamento da loja foi de : " + faturamento) -> Nesse formato, retornará erro, pois o + não concatena string com int por exemplo.
# É preciso converter de int para string da seguinte forma:
print("O faturamento da loja foi de : " + str(faturamento))
print()
# Uso do format
print("O faturamento foi de: {}".format(faturamento))
print("O faturamento foi de: {}. O custo foi de {} e o lucro foi de {}.".format(faturamento, custo, lucro))
print("O faturamento foi de: {0}. O custo foi de {1} e o lucro foi de {2}. Lembrando que o faturamento foi de {0}".format(faturamento, custo, lucro))
# Todos os formats devem ser preenchidos. Se colocar 0 em um, vc terá que preencher todos.
print()
# Uso do %s e %d
print("O faturamento foi de: %d." %(faturamento))
print("O faturamento foi de: %d, o custo foi de: %d, o lucro foi de: %d" %(faturamento, custo, lucro))
print("O meu email é: %s " %(email))
print()
# Uso do in
print("@" in "felipe@gmail.com")
print("@" not in "felipe@gmail.com")