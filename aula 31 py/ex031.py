'''d = int(input('digite a distancia da sua viagem:'))
if d <= 200:
    print('Vc vai percorrer {:.2f}KM , preço da sua passagem ficou R$75.00'.format(d))
else:
    d > 200
    print ('Vc vai percorrer {:.2f}KM , preço da sua passagem ficou R$94.50'.format(d))'''

distancia = float(input('Qual é a distancia da sua viagem?'))
print ('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))
