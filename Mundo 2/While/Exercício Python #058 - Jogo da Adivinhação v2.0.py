print('Jogo de adivinhação.')
from random import randint
computador=randint(0,3)
sair=False
contador=0
while not sair:
    jogador=(int(input('Digite um numero ')))
    contador+=1
    if jogador<computador:
        print('Chuta mais alto')
    if jogador > computador:
        print('Chuta mais baixo')
    if jogador == computador:
        sair=True

print(f'Parabens você ganhou o computador também pensou em {computador} e você demorou {contador} vez/vezes p/ acertar! ')
