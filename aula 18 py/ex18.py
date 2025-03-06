from math import radians , sin , cos , tan 
ang = float(input('digite o angulo que deseja:'))
seno = sin(radians(ang))
print ('o angulo de {} tem o seno de {:.2f}'.format(ang,seno))
co = cos(radians(ang))
print('o angulo de {} tem o cosseno de {:.2f}'.format(ang,co))
tan = tan(radians(ang))
print('o angulo de {} tem o tangente de {:.2f}'.format(ang,tan))