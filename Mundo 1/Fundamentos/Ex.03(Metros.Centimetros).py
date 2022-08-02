m = float(input('Distancia em metros: '))
cm = m * 100
mm = m * 1000
km = m / 1000

print('O valor de {} metros,convertido p/cm é {:.0f}cm\nO valor convertido para milimetros é {:.0f}mm\nO valor convertido p/ km é {}km\n'.format(m,cm,mm,km,))