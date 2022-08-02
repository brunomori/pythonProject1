cont= 'zero','um','dois','três','Quartro','Cinco','seis','sete','oito','nove','dez'
while True:

    numero=int(input('Digite um numero de 0 a 10'))
    if numero <= 10 and numero >= 0:
        break
    print('Tente novamente')
print(cont[numero])
print('Fim')
