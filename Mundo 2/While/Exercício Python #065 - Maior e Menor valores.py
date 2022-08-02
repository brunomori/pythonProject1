maior=0
menor=0
contador=0
continuar='S'
soma=0
while continuar in 'Ss':
    numero=int(input('Digite um numero'))
    continuar=str(input('Deseja continuar? [S/N]')).upper().strip()
    contador+=1
    soma+=numero
    media=soma/contador
    if contador==1:
        maior=numero
        menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero

print('Você digitou {} numeros, a soma de todos os numeros é {}, a media é {:.2f}, o menor numero foi {} e maior foi {}'.format(contador,soma,media,menor,maior))

