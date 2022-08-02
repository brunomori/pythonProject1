print('Hmmm vou aplicar um descontinho pra qlqr valor que você me pedir!')
p = float(input("Qual o preço do produto? "))
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(p, p-(p * 5 / 100)))






'''preço=int(input('Manda o preço do produto!: '))
descontão=int(input('Quantos % devo diminuir o preço do produto?: '))
discount=preço*(1-(descontão * 0.01))
print(f'Na liquidação, esse produto vale {discount} reais!')'''