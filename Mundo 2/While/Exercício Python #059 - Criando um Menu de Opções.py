print('Bem vindo a menu!')
n1=float(input('Digite o primeiro valor '))
n2=float(input('Digite o segundo valor'))
x=0
y=0
sair=False
while not sair:
    opção=int(input('''
    [1] Somar
    [2]Multiplicar
    [3]Maior
    [4]novos numeros
    [5] sair do programa'''))

    if opção==1:
        soma=n1+n2
        print('A soma dos numeros é {}'.format(soma))

    elif opção==2:
        multiplicar=n1*n2
        print('A multiplicação dos numeros é {}'.format(multiplicar))

    elif opção==3:
        x=n1
        y=n2
        if x>y:
            print('o numero maior é {}'.format(x))
        if y>x:
            print('O numero maior é {}'.format(y))

    elif opção==4:
        print('Seu desejo é uma ordem')
        n1=float(input('Digite o primeiro novo numero'))
        n2=float(input('Digite o segundo novo numero'))


    elif opção==5:
        sair=True

    else:
        print('Opção invalida, se deseja sair aperte o 5!')

print('Obrigado por usar nosso programa')