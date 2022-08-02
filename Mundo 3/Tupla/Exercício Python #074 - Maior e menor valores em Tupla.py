from random import  randint
lista=randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),
for n in lista:
    print(f'{n}',end=' ')
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')