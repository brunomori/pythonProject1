cont=0
n1=int(input('Digite um numero')),int(input('Digite um numero')),int(input('Digite um numero')),int(input('Digite um numero'))
print(f'Você digitou {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1} posição')
else:
    print('não existe o valor 3')
for n in n1:
    if n%2==0:
        print(n)
