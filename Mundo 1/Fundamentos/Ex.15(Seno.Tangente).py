#import math
#angulo = float(input('Digite o angulo que você deseja'))
#seno =math.sin(math.radians(angulo))

#print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
#cosseno=math.cos(math.radians(angulo))

#print('o angulo de {} tem o cesseno de {:.2f}'.format(angulo,cosseno))

#tangente = math.tan(math.radians(angulo))
#print('o angulo de {} tem a tangente de {:.2f}'.fomart(angulo,tangente))

#================================================================================
from math import  radians, sin ,cos ,tan
angulo = float(input('Digite o angulo que você deseja'))
seno = sin(radians(angulo))

print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno= cos(radians(angulo))
print('o angulo de {} tem o cesseno de {:.2f}'.format(angulo,cosseno))

tangente = tan(radians(angulo))
print('o angulo de {} tem a tangente de {:.2f}'.fomart(angulo,tangente))



#====================================================================================================
# import math
# an = float(input('digite o angulo q deseja?'))
# r = math.radians(an)
# s = math.sin(r)
# c = math.cos(r)
# t = math.tan(r)
# print('se o angulo for {} \n o seno sera {:.2f} \n o coseno sera{:.2f} \n e a trangente sera {:.2f}'.format(an, s, c, t))
