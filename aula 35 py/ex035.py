r1 = float(input('digite um nuemro:'))
r2 = float(input('digite um nuemro:'))
r3 = float(input('digite um nuemro:'))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os numeros formam um triangulo')
else:
    print('Não formam um triangulo')