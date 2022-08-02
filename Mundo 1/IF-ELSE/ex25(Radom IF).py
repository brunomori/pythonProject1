from random import randint
from time import sleep
computador = randint(0, 5)

n=int(input(' Em que numero eu pensei de 0 a 5 ? '))
print('-=-'*20)
print('Pensando ...')
sleep (1.5)
if n==computador:
    print('Eu tambem pensei no numero {}, você ganhou'.format(computador))
else:
    print('Eu pensei no numero {}, você perdeu'.format(computador))
print('-=-'*20)