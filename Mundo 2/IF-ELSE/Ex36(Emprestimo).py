print('Aprovar emprestimo')
casa=float(input('Digite o valor da casa'))
salario=float(input('Digte o valor do salario'))
anos=int(input('Digite em quantos anos deseja pagar'))
meses=anos*12
minimo= 30*salario/100
prestação=casa/meses

if prestação <= minimo:
    print('Parabens , seu emprestimo foi aprovado')
else:
    print('Desculpe seu emprestimo foi negado!')

