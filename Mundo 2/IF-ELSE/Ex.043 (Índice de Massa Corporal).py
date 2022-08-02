print('=*='*20)
print('Calculadora IMC by:Bruno Manzini')
peso=float(input('Digite seu peso'))
altura=float(input('Digite sua altura'))

imc=peso/(altura**2)

if imc < 18.5:
    print('Você esta abaixo do peso normal')

elif imc >=18.5 and imc<=25:
    print('Seu pso é normal')

elif imc >=25 and imc <=30:
    print('Sobrepeso')

elif imc >=30 and imc <=40:
    print('Obesidade')

#elif imc >= 40:
else:
    print('Obesidade morbida')
print('O IMC da pessoa seria {:.1f}'.format(imc))
