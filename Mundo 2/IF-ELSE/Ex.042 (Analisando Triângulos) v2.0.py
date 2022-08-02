print('-_'*20)
print('Analisador de triangulos')
r1=int(input('Digite o Primeiro segmento'))
r2=int(input('Digite o segundo segmento '))
r3=int(input('Digite o terceiro segmento '))

if r1 < r2 + r3 and r2 <r1 + r3 and r3 <r1+ r2:
    print(' é possivel fazer um triangulo')
    if r1==r2 and r2==r3:
        print('Equilátero')
    elif r1!= r2!= r3!=r1:
        print('Escaleno')
    else:
        print('issósceles')

