print('Tabuada 3.0')

while True:
    n = int(input('Digite um valor p/ saber a tabuada'))
    if n<0:
        break
    for lista in range(0,11):
        print(f'{n}x{lista}={n*lista}')
print('Obrigado por utilizar nosso programa , volte sempre!')

