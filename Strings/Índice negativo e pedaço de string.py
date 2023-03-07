"""
-16  -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
 f    e    l    i    p    e    @    g    m    a    i    l    .    c    o    m

Para pegar um texto de trâs pra frente: texto[indice] -> onde índice é negativo

Para pegar um pedaço de um texto use: (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]

"""

email = 'felipe@gmail.com'
nome = 'Felipe Guedes'

print(email[6:]) # @gmail.com
print(email[:6]) # felipe
print(email[5:8])# e@g

print("Tamanho do email " + str(len(email)) + " caracteres")
print("Primeiro caractere " + "? " +  (email[0]))
print("Ultimo caractere " + "? " + (email[-1]) )
print("Servidor do email " + "? " + email[6:12])
