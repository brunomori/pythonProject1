v=float(input('Digite a velocidade do caro'))

if  v >=81:
    print('Você foi multado')
    v1 = (v - 80) * 7
    print('Sua multa então sera de R${:.2f}'.format(v1))

else:
    print('Você não foi multado, parabens')

