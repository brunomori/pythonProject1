a=int(input('Digite o Primeiro valor'))
b=int(input('Digite o Segundo valor'))
c=int(input('Digite o terceiro valor'))


#menor=a

if a<b and a<c:
    menor= a

if b<a and b<c:
    menor=b

if c<a and c<b:
    menor=c

print('O menor valor foi {} '.format(menor))
#maior=a
if a>b and a>c:
    maior= a

if b>a and b>c:
    maior=b

if c>a and c>b:
    maior=c
print('o maior numero digitado foi {}'.format(maior ))
