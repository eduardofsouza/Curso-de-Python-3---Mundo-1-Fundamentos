dias = int(input('quala quantidade de dias q ele foi alugado'))
km = float(input('quantos km percorridos por um carro alugado?'))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de {:.2f}'.format(pago))

