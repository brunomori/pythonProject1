produto=int(input('Digite o valor do produto'))
print('''
[1] à vista dinheiro/cheque: 10% de desconto
[2]à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
''' )
opção=int(input('Qual opção você deseja?'))

if opção==1:
    dproduto= produto*10/100
    print('preço do produto ficou: R${:.2f}'.format(dproduto))

elif opção==2:
    dproduto=produto*5/100
    print('preço do produto ficou:R${:.2f}'.format(dproduto))

elif opção==4:
    Q=int(input('em quantas vezes?'))
    if Q <= 2:
        juros=produto/Q
        print('O preço sai formal e dividimos sem juros! ficou R${}'.format(Q))
    elif Q >=3:
        juros=produto+(produto*20/100)
        print('o preço do produto saiu {}'.format(juros))
else:
    print('opção invalida')
    exit()