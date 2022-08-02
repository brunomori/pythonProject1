lista=list()
while True:
    nome=str(input('Nome:'))
    n1=float(input('Nota 1ª:'))
    n2=float(input('Nota 2º'))
    media=(n1+n2)/2
    lista.append([nome,[n1,n2],media])
    continuar=str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if continuar=='N':
        break
print('-'*20)
print(f'{"Nº":<4}{"Nome":<6}{"Media":<8}')
for indece, a in enumerate(lista):
    print(f'{indece:<4}{a[0]:<6}{a[2]:<8}')
print('-'*20)
while True:
    qual=int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if  qual==999:
        print('Finalizando...')
        print('>>>Volte Sempre<<<')
        break
    if qual <= len(lista)-1:
        print(f'Nostas de {lista[qual][0]} são {lista[qual][1]}        ')


