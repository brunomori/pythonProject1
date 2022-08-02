print('='*15)
print('LOJA SUPER BARATÃO')
print('='*15)
continuar=''
total=0
ProdutoMil=0
contador=0
ProdutoBarato=0
NomeBarato=''
Nome='' ## Acrescentei essa linha
while True:
  Nome=input('Nome Produto:')
  Preço=float(input('Preço: R$'))
  total+=Preço
  if Preço>1000:
    contador+=1
    ProdutoBarato=Preço
    NomeBarato=Nome
  if Preço<ProdutoBarato:
    ProdutoBarato=Preço
    NomeBarato = Nome
  
  continuar=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
  if continuar=='N':
    break
    
print(f'O total das compras foi R${total:.2f}')
print(f'Temos {contador} produtos custando mais de R$1000.00')
print(f'O nome do produto mais barato é {NomeBarato}e custa R${ProdutoBarato}')