'''import random

numero = int(input('digite um nuemro:'))
aleatorio = random.randint(0,10)
if aleatorio == numero:
    print('parabens')
else:
    print ('errou')'''

from random import randint
from time import sleep
computador = randint (0,5)
print('tente adivinhar em que numereo pensei:')
j = int(input('Em que numero pensei?'))
print('Processando...')
sleep(3)
if j == computador:
    print ('vc acertou, para bens!')
else:
    print ('Errou o q eu estava pensando era {}!'.format(computador))