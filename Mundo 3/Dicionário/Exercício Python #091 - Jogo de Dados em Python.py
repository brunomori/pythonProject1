from random import  randint
from time import  sleep
from operator import  itemgetter #ordernar print das chaves por valores
jogo={'Jogador(1)':randint(1,6),
      'Jogador(2)':randint(1,6),
      'Jogador(3)':randint(1,6),
      'Jogador(4)':randint(1,6),
      }
rank={}
print('Valores sorteados:')
print('-='*20)
for chave,valor in jogo.items():
    print(f'O {chave}, tirou >{valor}<')
    sleep(0.5)
print('-='*20)
rank=sorted(jogo.items(),key=itemgetter(1),reverse=True)   #sorted(jogo.items() )= vai ordernar //  key=itegetter(1) vai ordernar os randint.
print('===Ranking dos Jogadores===')
for indece, valor1 in enumerate(rank):
    print(f'{indece+1}º lugar: {valor1[0]} com {valor1[1]}')