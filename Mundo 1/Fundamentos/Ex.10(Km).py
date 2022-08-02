#print('Alugel de carro')
#dias=float(input('Quandidade de dias'))
#km=float(input('Qual foi o km percorrido ?'))
   # rdia= dias* 60
  #  rkm=  km* 0.15
 #       pago=rkm+rdia

#print('O aluguel ficou R$:{:.2f} \nSendo que o dias ficaram {:.2f} \nos kms{:.2f}'.format(pago,rdia,rkm))

dias = int(input('Quantos dias de locação? '))
km = float(input('Quantos KM rodados? '))
sd = (dias * 60) + (km * 0.15)
print(f'O saldo devedor é R$:{sd}')