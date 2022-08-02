n=int(input('Digite um numero'))
tot=0
for lista in range (1,n+1):
    if n%lista==0:
        print('\33[34m',end=' ')
        tot+=1
    else:
        print('\33[31m',end= ' ')
    print('{}'.format(lista),end=' ')
print('\n\033[ O numero {} foi divisivel {} vezes'.format(n,tot))
if tot ==2:
    print('O numero é primo')
else:
    print('o numero não é primo')


#numero primo é divisivel por 1 e por eles mesmo