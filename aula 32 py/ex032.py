'''ano = int(input('digite o ano:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano é bissexto')
else:
    print('O ano não é bissexto')'''

from datetime import date 
ano = int(input('digite o ano ou para saber o ano atual digite "0":'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))