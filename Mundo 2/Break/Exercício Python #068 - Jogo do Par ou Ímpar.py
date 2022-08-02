from random import randint
v=0
while True:
    jogador=int(input('Digite um valor'))
    computador=randint(0,10)
    total=jogador+computador
    tipo= ''
    while tipo not in 'PI':
        tipo=str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Você  jogou {jogador} e o computador {computador}. Total é de {total}')
    print('Deu par'if total%2==0 else 'Deu impar')
    if tipo =='P':
        if total %2==0:
            print('Você ganhou')
            v+=1
        else:
            print('Você perdeu')
            break

    elif tipo =='I':
        if total %2==1:
            v+=1
            print('Você ganhou')
        else:
            print('Você perdeu')
    print('Vamos jogar novamente')
print(f'Game over! Você venceu {v}vezes.')