'''nome = str(input('digite seu nome:')).strip()
if nome == 'Eduardo':
    print ('bonito nome!')
else:
    nome == 'Maria'
    print ('Seu nome é comum {}'.format(nome))
print ('bom dia, {}'.format(nome))'''

n1 = float(input('digite a primeira nota:'))
n2 = float(input('digite a segunda nota:'))
m = (n1 + n2 )/2
print ('sua media foi {:.1f}'.format(m))
if m >= 6:
    print ('boa media')
else:
    print ('vc repetiu')