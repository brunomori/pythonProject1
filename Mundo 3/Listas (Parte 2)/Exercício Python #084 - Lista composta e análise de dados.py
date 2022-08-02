lista=list()
contador=0
principal=[]
maior=0
menor=0
while True:
    lista.append(str(input('Nome:')))
    lista.append(int(input('Peso:')))
    if len(principal)==0:
        maior=lista[1]
        menor=lista[1]
    else:
        if lista[1]>maior:
            maior=lista[1]

        if lista[1]<menor:
            menor=lista[1]

    principal.append(lista[:])
    lista.clear()
    contador+=1
    continuar=str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if continuar=='N':
        break
print(f'Ao todo, você cadastrou {contador} pessoas ')
print(f'O maio peso foi de {maior}KG.')
for p in lista:
    if p[1]==maior:
        print(f'{p}')
print(f'O menor peso foi de {menor}KG')
