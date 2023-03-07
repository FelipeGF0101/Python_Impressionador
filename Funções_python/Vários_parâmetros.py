"""
Mais de 1 argumento e formas de passar argumento para uma função

Estrututra:

* 2 formas de passar o argumento
    1 - Em ordem (positional argument)
    2 - Com o nome do argumento (keyword argument)

* Vamos mudar a função que fizemos na aula passada para conseguir categorizar qualquer tipo de bebida 
de acordo com o "rótulo" passando para a nossa function. Basicamente nossa function agora tem que verificar
se o produto é da categoria passada ou não.

"""
# Em ordem (positional argument)

def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
    
produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

for produto in produtos:
    if categoria(produto, 'BEB'):
        print(f'Enviar {produto} para o setor de bebidas alcóolicas.')
    elif categoria(produto, 'BSA'):
        print(f'Enviar {produto} para o setor de bebidas não alcóolicas.')

print()

# Com o nome do argumento (keyword argument)

def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
    
produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

for produto in produtos:
    if categoria(cod_categoria = 'BEB', bebida = produto):
        print(f'Enviar {produto} para o setor de bebidas alcóolicas.')
    elif categoria(produto, 'BSA'):
        print(f'Enviar {produto} para o setor de bebidas não alcóolicas.')

print()

# Antes do parâmetro de chave/texto, é possível usar o parâmetro por posição. Mas a paritr do momento em que 
# se usa o parâmetro por chave/texto, não se pode mais usar o parâmetro por posição.

qtde_produtos = len(produtos)
print("Quantidade total de produtos:", qtde_produtos, "texto2", "texto3", sep = '\n')

# Se fosse da forma abaixo, resultaria erro:

#qtde_produtos = len(produtos)
#print("Quantidade total de produtos:", qtde_produtos, "texto2", sep = '\n',"texto3" )