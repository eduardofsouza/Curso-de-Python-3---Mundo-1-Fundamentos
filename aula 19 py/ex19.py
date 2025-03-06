import random 
n1 = str(input('primeiro nomoe'))
n2 = str(input('segundo nomoe'))
n3 = str(input('terceiro nomoe'))
n4 = str(input('quart nomoe'))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))