numero= [[],[]]
valor=0
for c in range(1,8):
    valor=int(input('Digite um valor'))
    if valor%2==0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print(f' numeros pares são {numero[0]}')
print(f' numeros impares são {numero[1]}')
