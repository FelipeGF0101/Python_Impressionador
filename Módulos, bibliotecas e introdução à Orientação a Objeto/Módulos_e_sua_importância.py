"""
O que são Módulos e qual a importância deles?

Importância
* Já tem muita coisa pronta, então você não precisa criar do zero.
* Se você souber usar Módulos e como usar um módulo novo, você vai conseguir fazer praticamente tudo no Python

Estrutura Básica

import módulo

ou 

import módulo as nome

"""

# Exemplo: Como pode fazer o nosso código abrir um site específico na internet?

import webbrowser

webbrowser.open('https://www.google.com')

# Também é possível dar um "Apelido" ao módulo
# Poderia ser:
# import webbrowser as wb
# wb.open('https://www.google.com')

"""
VARIAÇÕES

# importar o módulo sem precisar usar o nome dele
from modulo import

# importar apenas algumas partes do módulo
from modulo import funcao1, funcao2 etc.
"""
