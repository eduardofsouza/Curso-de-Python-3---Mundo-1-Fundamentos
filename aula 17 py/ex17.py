#co = float(input('comprimento do cateto oposto'))
#ca = float(input('comprimento do cateto adjacente'))
#hi = (co * 2 + CA ** 2) ** (1/2)
#print('A hopotenusa vai medir {:.2f}'.format(hi))
import math 
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente'))
hi = math.hypot(co , ca)
print('A hopotenusa vai medir {:.2f}'.format(hi))
