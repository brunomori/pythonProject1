soma = 0
for lista in range(0,7):
    numero=int(input('Digite o valor {}: '.format(lista)))
    if numero %2==0:
        soma=soma+numero
print(soma)


