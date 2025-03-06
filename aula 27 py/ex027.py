n = str(input('digite seu nome:')).strip()
print('seu nome é: {}'.format(n))
print ('seu primeiro nome é: {}'.format(n.split()[0]))
print ('seu ultimo nome é: {}'.format(n.rsplit()[-1]))
 