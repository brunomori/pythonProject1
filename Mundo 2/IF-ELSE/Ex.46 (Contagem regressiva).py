from time import sleep
nome=str(input('Vendedor Vindo.....\n OLÁ! Qual é o seu nome?'))

sexo=str(input('{} você é homem ou mulher?'.format(nome)).upper())

if sexo=='MULHER':
    compra=int(input('''Estou vendendo fogos, a SENHORA {} gostaria de compra?
[0] SIM
[1] NÃO'''.format(nome)))
    if compra == 1:
        print('Desculpe incomodar')
        exit()

    if compra == 0:
        quantidade = int(input('Otimo, os fogos custam R$ 1,00 cada.\n Quantos a senhora vai querer? >>>LIMITE 10<<<'))
        if quantidade <= 10:
            fogos = 1
            preço = quantidade * fogos
            print('{} a senhora vai querer {} fogos  e vai ficar R$ {} Reais '.format(nome, quantidade, preço))

        else:
            print('Desculpe eu só tenho 10 para vender ')
            exit()
    else:
        print('Reposta incorreta, adeus')
        exit()
if sexo=='HOMEM':
    compra=int(input('''Estou vendendo fogos, o SENHOR {} gostaria de compra?
    [0] SIM
    [1] NÃO'''.format(nome)))
    if compra==1:
        print('Desculpe incomodar')
        exit()

    if compra == 1:
        print('Desculpe incomodar')
        exit()

    if compra == 0:
        quantidade = int(input('Otimo, os fogos custam R$ 1,00 cada.\n Quanto o senhor vai querer? >>>LIMITE 10<<<'))
        if quantidade <= 10:
            fogos = 1
            preço = quantidade * fogos
            print('{} o senhor vai querer {} fogos  e vai ficar R$ {} Reais '.format(nome, quantidade, preço))

        else:
            print('Desculpe, eu só tenho 10 para vender ')
            exit()

    else:
        print('Reposta incorreta, adeus')
        exit()

permissão=int(input('''Vai querer estourar todos seus fogos?
[1] SIM! (VAI ACONTECER ALGO LEGAL!)
[2] NÃO ( TU É UM CHATO)'''))
if permissão==1:
        for lista in range(0, quantidade + 1, 1):
                print(lista)
                print('BUMMMM\nKABUM')
                sleep(0.9)
        print('Seus fogos acabou , compre mais amanhã!!!')
if permissão==2:
        print('bye seu chatão')




              #LISTA#
#  0 Começar a contagem p/ estourar os folgos.
#  Quantidade total de folgos.
#  Somar mais um apenas
#  1 Pular um por vez.

