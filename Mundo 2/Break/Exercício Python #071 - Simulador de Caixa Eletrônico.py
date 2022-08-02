valor=int(input('Quanto deseja sacar'))
sac=valor
nota1=0
nota10=0
nota20=0
nota50=0
continuar=''
continuar=True
while not continuar:
    while sac >=50:
        sac-=50
        nota50+=1
    while sac>=20:
        sac-=20
        nota20+=1
    while sac>=10:
        nota10+=1
    while sac>=1:
        sac-=1
        nota1+=1
        print(f'Você usou {nota50} notas de 50.')
        print(f'Você usou {nota20} notas de 20')
        print(f'Você usou {nota10} notas de 10')
        print(f'Você usou {nota1}  notas de 1')

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar=='Nn':
        continuar=False

