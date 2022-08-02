n=int(input("Digite um numero inteiro p/ converter"))
print('''Escolha uma das bases para conversão:
[1]Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

v= int(input('Sua opção:'))

if v==1:
    print('Resultado p/ BINARIO:{}'.format(n,bin(n)))
elif v==2:
    print('Resultado p/ OCTAL: {}'.format(n,oct(n)))
elif v==3:
    print('Resultado p/ HEXADECIMAL: {}'.format(n,hex(n)))

else:
    print('Opção invalida ANIMAL')