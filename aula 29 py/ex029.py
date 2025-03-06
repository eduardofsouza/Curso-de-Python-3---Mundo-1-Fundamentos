'''velo = float(input('A quantos KM vc estava?'))
limite = 80
multa = 7
if velo > 80:
    print (' MULTADO!, Voce excedeu o limite de 80km, sua velocidade foi:{:.1f}'.format(velo))
    kmA = velo - limite
    multa = kmA * multa
    print ('vc tera que pagar uma multa de {}'.format(multa))
else:
    print('esta tudo certo!')'''

velo = float(input('Qual é a velocidade do carro?'))
if velo > 80:
    print('MULTADO! Você excedeu o limite de valocidade de 80km/h')
    multa = (velo - 80 ) * 7
    print('Você deve pagar uma multa de {:.2f}!'.format(multa))
print ('Bom dia! diriga com segurança!')