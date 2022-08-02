lista=[]
while True:
    n=int(input('Digite um numero'))
    if n not in lista:
        lista.append(n)
        print('Numero gravado com sucesso.')
    else:
        print('numero repetido , não vou gravar!')

    continuar=str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar!='S':
        break
lista.sort()
print(f'os numeros na ordem digitados foram {lista}')