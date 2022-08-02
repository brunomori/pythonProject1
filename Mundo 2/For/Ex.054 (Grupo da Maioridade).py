maior=0
menor=0

for y in range (1,7):
    peso=float(input('Digite o peso da {}º pessoa'.format(y)))

    if y==1:
        menor=peso
        maior=peso
    else:
        if peso>maior:
            maior=peso

        if peso<menor:
            menor=peso

print('o menor peso foi {}'.format(menor))
print('o maior peso foi {}'.format(maior))