real=float(input('Olá, irmão quanto dinheiro você tem na carteira ?'))

dolar=real/5.17

print('Você sabia que essa sua grana em dolar é ${:.2f}?'.format(dolar))


print('Vamos agora falar sobre construção , que tal saber a area de um comodo e quanto de tinta é necessario para pintar tudo!')
a1=float(input("Digite quantos metros de largura tem a parede"))
a2=float(input('Digite quantos metros tem de altura a  parede'))
a3=a1*a2
print('Sua parede te, a dimensão de {}x{} e sua área é de {}m'.format(a1,a2,a3,))
tinta =a3/2
print('Para pintar essa parede você ira precisar de {} litros'.format(tinta))
