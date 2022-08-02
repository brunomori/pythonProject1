listagem='Lapis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Caneta',22.30,'Livro',34.90

for pos in range(0,len(listagem)):
    if pos %2==0: #descubrir se é par
        print(f'{listagem[pos]:.<30}',end='')  #alinhar a esquerda, #nistrar 30 caracteres
    else:
        print(f'R${listagem[pos]:>10.2f}')  #2f para deixar com numero em diheiro

