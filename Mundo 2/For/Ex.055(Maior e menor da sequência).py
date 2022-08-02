#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor=0
maior=0
for y in range (1,6):
    peso=float(input('Digite o peso {}ºpessoa'.format(y)))

    if y==1:
        menor=peso
        maior=peso
    else:
        if peso>maior:
            maior=peso

        if peso < menor:
            menor=peso
print('De todos os pesos digitados o menor foi {:.2f} e o maior foi {:.2f} '.format(menor,maior))