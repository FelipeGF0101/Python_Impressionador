"""
Exceções e Erros em Funções

Como "testar" erros e tratar exceções:

try:
    O que eu quero tentar fazer
except:
    O que vou fazer caso dê erro
"""
def descobrir_servidor(email):
    try: # Tente fazer isso...
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
    
    except: # caso não consiga, retorne isso:
        print("Email digitado não tem @. Por favor, digite novamente!")
   
email = input('Qual o seu e-mail? ')
print(descobrir_servidor(email))

# OBS: Cuidado, uma vez dentro do try, qualquer erro vai levar ao except.

# COMO PRINTAR UM ERRO EM UMA FUNCTION
"""
raise Exception('O erro foi esse')

ou então avisando qual o tipo de erro que ele teve

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse')
"""
def descobrir_servidor(email):
    try: # Tente fazer isso...
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
    except: # caso não consiga, retorne isso:
        # O raise Exception te da a opção de personalizar a mensagem de erro.
        raise Exception("Email digitado não tem @. Por favor, digite novamente!")
        # Também é possível trocar o nome do erro. Por exemplo: 
        # raise ValueError("Email digitado não tem @. Por favor, digite novamente!")
    
# Tratamento Completo:

"""
try:
    tente fazer isso
except ErroEspecífico:
    deu esse erro aqui que era esperado 
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.
"""

def descobrir_servidor(email):
    try: # Tente fazer isso...
        posicao_a = email.index('@')
    except: # Talvez dê esse erro.(Erro esperado)
        raise ValueError('Email digitado não tem @. Digite novamente...')  
    else: # Caso não dê erro esperado, rode isso aqui...
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
    # finally Vai rodar independente do que acontecer
    # ... código

   
email = input('Qual o seu e-mail? ')
print(descobrir_servidor(email))