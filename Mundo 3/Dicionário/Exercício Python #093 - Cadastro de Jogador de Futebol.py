time=list()
jogador=dict()
partidas=list()

while True:
    jogador.clear()
    jogador['Nome']=str(input('Nome do jogador:'))
    tot=int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c}')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar?')).strip().upper()[0]
        if continuar in "SN":
            break
        print('Reposta invalida!')
    if continuar=='N':
        break

print('-'*40)
print('Cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)

for key,valor in enumerate(time):
    print(f'{key:>3}',end='')
    for d in valor.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)

while True:
    buscar=int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if buscar==999:
        break
    if buscar>=len(time):
        print(f'ERRO! Não existe jogador com o codigo {buscar}')
    else:
        print(f' Levantamento do jogador {time[buscar]["nome"]}:')
        for i,g in enumerate(time[buscar]['gols']):
            print(f' No jogo {i} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE>>>')













