num = int(input ('escreva um numero inteiro'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('seu numero é {}:'.format(num))
print ('{} é unidade'.format(u))
print ('{} é dezena'.format(d))
print ('{} é centena'.format(c))
print ('{} é milhar'.format(m))