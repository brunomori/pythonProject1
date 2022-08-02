print('Gerador de PA')
termo=int(input('Digite o primeiro termo'))
razão=int(input('Digite a razão'))
contador=0

while contador<10:
    print(f'{termo}=>',end='')
    contador+=1
    termo+=razão
print('fim')