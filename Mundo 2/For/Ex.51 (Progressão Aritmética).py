print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

r1=int(input('Primeiro termo'))
r2=int(input('Razão'))
decimo=r1+(10-1)*r2

for c in range(r1,decimo + r2,r2):
    print('{}'.format(c),end='>')
print('Finish')
