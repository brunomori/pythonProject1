print('Blaze 2.0')
parar=''
win=''
while True:

    banca=int(input('Digite a banca'))
    bancaCorreta=banca/100*3
    print(f'Sua banca é {banca} e você deve começar com entrada no valor de {bancaCorreta:.2f}')


    entrada=int(input('Digite a primeira entrada'))
    branco=entrada/100*18
    print(f'Entre com {branco:.2f} no branco ')

    gal1valor=entrada+entrada+bancaCorreta
    branco2=entrada+branco/100*18
    print(f'Você deve jogar no gali 1 // {gal1valor:.2f}, entre no branco com {branco2:.2f}')


    gal2valor=gal1valor+gal1valor+bancaCorreta
    branco3=entrada+branco2/100*18
    print(f'Você deve jogar no gali 2// {gal2valor:.2f}, entre no branco {branco3:.2f}')

    while True:
        win=int(input('Deu win na 1º , 2º ou na 3º?Caso não queira saber, digite 0 p/ sair!'))
        if win==1:\
            print('Ganhou de primeira')
        elif win==2:
            print('Ganhou de segunda')
        elif win==3:
            print('Ganhou de terceira')
        elif win=='0':
            break
        else:
            print('Opção invalida')


    parar=str(input('Deseja parar [S/N]')).upper().strip()

    if parar == 'sS':
        break







