medida = float(input('uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
dm = medida * 10
um = medida * 1000000
nm = medida * 1000000000
print ('a medida de {}m corresponde a {:.0f}cm e {:.0f}mm e {:.0f}km e {:.0f}dm e {:.0f}um e {:.0f}nm'.format(medida, cm , mm , km , dm , um , nm))