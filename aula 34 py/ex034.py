s = float(input('digite o salario:'))

if s >= 1250:
    a =(10 / 100) * s
    s += a
    print ('porcentagem de aumento foi de 10% , e seu salario é R${:.2f}'.format(s))
else:
    s < 1250
    a =(15 / 100) * s
    s += a
    print ('porcentagem de aumento foi de 15% , e seu salario é R${:.2f}'.format(s))