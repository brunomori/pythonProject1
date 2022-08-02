maior=0
menor=0
lista=[]

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}')))
    if c==0:
        menor=lista[c]
        maior=lista[c]
    else:
        if lista[c]<menor:
            menor=lista[c]
            maior=lista[c]
        if lista[c]>maior:
print(f'Você digitou os valores {lista}')

print(f'O mair valor digitado foi {maior} na posição(s) é: ')

for a ,s enumerate(lista):
    if s==maior:
        print(f'A maior posição foi {a}')

for d,f enumerate(lista):
    if f==menor:
        print(f'A menor posição foi a {d}')





