'''from math import factorial
n= int(input('Digite o numero p/ calcular o fatorial'))
f=factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''

# Fatorial com While
n= int (input('Digite um numero para cacular seu  fatorial'))
c= n
f=1 #fatorial multiplicação limpa tem que ser 1 para ele se manter
while c>0:
    print('{}'.format(c),end='')
    print('x' if c >1 else '=',end='')
    f= f*c
    c -=1
print('{}'.format(f))