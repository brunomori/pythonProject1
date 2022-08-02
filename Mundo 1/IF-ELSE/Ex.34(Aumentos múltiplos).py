no=(input('Digite o nome do funcionario'))
s=float(input('Digite o salario do funcionario '))
if  s <=1250:
    n= s+(s*15/100)
    print('O funcionario {} tinha salario antigo de R${:.0f} e o salario novo é R${:.0f}'.format(no,s,n))
else:
    n= s+(s*10/100)
    print('O funcionario {} , tinha um salario antigo de R${:.0f} e o novo salario é R${:.0f}'.format(no,s,n))

