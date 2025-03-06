salario = float(input('digite seu salario: R$'))
aumento = float(input('digite seu aumento: %'))
salario_aumento = salario + (salario * aumento / 100)
print ('O seu salario atual é:{:.2f} , com o aumento de:{}% vai ser:{:.2f}'.format(salario , aumento , salario_aumento))