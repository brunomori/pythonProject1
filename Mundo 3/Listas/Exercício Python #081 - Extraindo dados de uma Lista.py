continuar=0
lista=[]
elemento5=False
contador=0

while True:
    n=int(input('Digite um numero'))
    if n==5:
        elemento5=True

    contador+=1
    lista.append(n)
    continuar=str(input('Deseja continuar[S/N]')).upper().strip()[0]
    if continuar=='N':
        break

print(f'Você digitou {contador} elementos')
if elemento5==True:
    print('Existe o valor 5 na lista')
else:
    print('Não existe o valor 5 na lista')
lista.sort(reverse=True)
print(f'Os valores decrecentes são {lista} ')
