from random import shuffle 
n1 = str(input('primeiro nome:'))
n2 = str(input('segundo nome:'))
n3 = str(input('terceiro nome:'))
n4 = str(input('quart nome:'))
lista = [n1 , n2 , n3 , n4]
shuffle(lista)
print ('a ordem de apresentacao sera: {}'.format(lista))
