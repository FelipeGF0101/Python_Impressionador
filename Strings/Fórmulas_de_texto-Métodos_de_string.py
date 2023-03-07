"""
"Fórmulas" de texto - métodos de string

Estrutura:
* Normalmente usamos a estrutura texto.método() para fazer as modificações que queremos
* Alguns métodos pedem "argumentos", que são informações que temos que passar para a fórmula (método) para ela funcionar.
Esses argumentos são passados dentro do parênteses.

Como usar:
Não decore os métodos, o que você for mais usando ocom o tempo você vai decorar o que precisar.
Mas a dica é: use essa lista para consulta e busque entender como o métodos funcionam e suas aplicações, para poder consultar e usar quando precisar.


"""

# capitalize() -> Coloca a 1ª letra maiúscula

texto = 'felipe'
print(texto.capitalize())
# resultado: Felipe
print()

# casefold() -> Tranforma todas as letras em minúsculas (existe o lower() mas o casefold é melhor normalmente.)
texto1 = "FELIPE"
print(texto1.casefold())
print(texto1.lower())
# resultado: felipe
print()

# count() -> Quantidade vezes que um valor aparece na string
texto2 = 'Felipe Guedes'
print(texto2.count('e'))
# resultado: 4
print()

# endswith() -> Verifica se o texto termina com um valor especifico e dá como resposta True ou False
texto3 = "felipe@gmail.com"
print(texto3.endswith('@gmail.com'))
# resultado: True
print()

# find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado
texto4 = 'felipe123@gmail.com'
print(texto4.find('@'))
# resultado: 9
print()

# isalnum() -> Verifica se um texto é todo feito com caraters alfanuméricos (letras e números) -> letras com acento ou ç 
# não são consideradas letras para essa função.
texto5 = 'felipe234'
print(texto5.isalnum())
# resultado: True
print()

# isalpha() -> verifica se um texto é todo feito de letras
texto6 = 'Felipe'
print(texto6.isalpha())
# resultado: True
# Porém, se tiver espaço entre os textos, o resultado é False.
print()

# replace() -> Substitui um texto por um outro texto em uma string
texto7 = '1000.00'
print(texto7.replace('.',','))
# resultado: 1000,00
print()

# split() -> Separa um string de acordo com um demilitador em vários textos diferentes
texto8 = 'felipe@gmail.com'
print(texto8.split('@'))
# resultado: ['felipe', 'gmail.com']
print()

# splitlines() -> Separa um texto em vários textos de acordo com os "enters" do texto
texto9 = '''Olá, bom dia! 
venho por meio deste email lhe informar o faturamento da loja no dia de hoje.
Faturamento = R$ 2.500,00'''
print(texto9.splitlines())
# resultado: ['Olá, bom dia! ', 'venho por meio deste email lhe informar o faturamento da loja no dia de hoje.', 'Faturamento = R$ 2.500,00']
print()

# startswith() -> Verifica se a string começa com determinado texto
texto10 = "BEB123"
print(texto10.startswith('BEB'))
# Resultado: True
print()

# strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no inicio e no final.
texto11 = '   BEB12345RG            '
print(texto11.strip())
# Resultado: BEB12345RG
print()

# title() -> Coloca a 1ª letra de cada palavra em maiúscula
texto12 = 'felipe guedes'
print(texto12.title())
# Resultado: Felipe Guedes
print()

# upper() -> Coloca o texto todo em maiúsculo
texto13 = 'Eu tenho um bulldog francês'
print(texto13.upper())
# Resultado: EU TENHO UM BULLDOG FRANCÊS
print()

# isnumeric() -> Verifica se a string só tem números
texto14 = "8663325"
print(texto14.isnumeric())
# Resultado: True