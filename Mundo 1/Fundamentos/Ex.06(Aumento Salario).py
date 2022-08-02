no=(input('Digite o nome do funcionario'))
s=float(input('Digite o salario do funcionario '))
r=float(input('Digite o valor desejado em % de aumento'))
n= s+(s*r/100)
print('O funcionario {} tinha salario antigo de R${:.0f} e o salario novo é R${:.0f}'.format(no,s,n))

