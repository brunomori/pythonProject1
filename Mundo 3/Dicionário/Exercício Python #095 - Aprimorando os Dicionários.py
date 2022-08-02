jogador=dict()
partidas=list()
jogador['Nome']=str(input('Nome do jogador:'))
tot=int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}')))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print(jogador)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print(f'O jogador {jogador["Nome"]} jogou {tot} partidas.')
for indece, valor in enumerate(jogador["gols"]):
    print(f' => Na partida {indece}, fez {valor} gols')
print(f'Foi um total de {jogador["total"]} gols.')



