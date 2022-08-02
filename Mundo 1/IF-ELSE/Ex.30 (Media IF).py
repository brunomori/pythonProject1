n1=int(input('Digite a primeira nota'))
n2=int(input('Digite a segunda nota'))

m=(n1+n2)/2

print('A media é {}'. format(m))
if m>=8:
    print('PARABENS VOCÊ PASSOU!')
else:
    print('Burro reprovou')