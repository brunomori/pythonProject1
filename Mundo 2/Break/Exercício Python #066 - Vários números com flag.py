'''
soma=0
contador=0

while True:
    numero=int(input('Digite um numero'))
    contador+=1
    soma+=numero
    if numero==999:
        break
print('Analisando')
print(f'Você fez o ciclo {contador} vezes e a soma de todos os numeros é {soma-999}')
'''


soma=0
contador=0

while True:
    numero=int(input('Dite um numero, digete 999 para parar!'))
    if numero == 999:
        break
    contador+=1
    soma+=numero

print(f'você fez o ciclo {contador} vezes, e a soma deles é {soma}')
