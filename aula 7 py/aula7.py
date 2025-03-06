#5 + 2 = 7
#5 - 2 = 3
#5 * 2 = 10
#5 / 2 = 2.5
#5 ** 2 = 25
#5 // 2 = 2
#5 % 2 = 1

#ordem de precedência
#1 ()
#2 **
#3 *,/,//,%
#4 +,-

n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m = n1 + n2 / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1,n2,m))