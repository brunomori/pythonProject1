lista=[]
par=[]
impar=[]
continuar=''

while True:
    n=int(input('Digite um numero'))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar=str(input('Deseja continuar[S/N]:')).strip().upper()[0]
    if continuar!='S':
        break
print(f'A lista completa é {lista}')
print(f'Os numeros impares são {impar}')
print(f'Os numeros pares são {par}')