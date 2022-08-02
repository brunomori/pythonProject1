''' Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
 parta viagens mais
 longas.'''

d=float(input('Digite a distancia da viagem em KM'))
print('Você está preste a começar uma viagem de tantos {:.2f}KM! Pronto ? '.format(d))
if d <= 200:
    d1=d*0.50

else:
    d1=d*0.45
print('O preço da sua passagem é R${:.2f}'.format(d1))
