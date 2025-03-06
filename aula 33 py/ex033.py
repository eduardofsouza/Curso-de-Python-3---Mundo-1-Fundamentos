n1 = int(input('primeiro um numero:'))
n2 = int(input('segundo um numero:'))
n3 = int(input('terceiro um numero:'))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    menor = n3
print('O maior valor digitado foi {}!'.format(maior))
print('O menor valor digitado foi {}!'.format(menor))