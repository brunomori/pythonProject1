from random import randint
itens=('Pedra','Papel','Tesoura')
pc=randint(0,2)
player=int(input('''O que você vai jogar?
[0]PEDRA
[1]PAPEL
[2]TESOURA
'''))

print('Computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[player]))

if pc==0: #pedra
    if player ==0:
        print('Empate')
    if player==1:
        print('Vitoria')
    if player==2:
        print('Derrota')

if pc==1: #papel
    if player ==0:
        print('Derrota')
    if player==1:
        print('Empate')
    if player==2:
        print('Derrota')

if pc==2: #tesoura
    if player ==0:
        print('Vioria')
    if player==1:
        print('Derrota')
    if player==2:
        print('Empate')

print('\nVolte Sempre!')