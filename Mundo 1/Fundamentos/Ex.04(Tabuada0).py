#n=int(input('Digite um numero para ver sua tabuada:\n'))

#n1= n * 1
#n2= n * 2
#n3= n * 3
#n4= n * 4
#n5= n * 5
#n6= n * 6
#n7= n * 7
#n8= n * 8
#n9= n * 9
#n10= n * 10

#print(f'=========================\n{n}x1={n1}\n{n}x2={n2}\n{n}x3={n3}\n{n}x4={n4}\n{n}x5={n5}\n{n}x6={n6}\n{n}x7={n7}\n{n}x8={n8}\n{n}x9={n9}\n{n}x10={n10}\n=========================')
#print('Obrigado por usar nossa tabuada, tmj <3')

n=int(input('Digite um numero para ver sua tabuada'))
print('-'*12)
print('{}x{:2}={}'.format(n,1,n*1))  #('{}x{:2}={}' para ter dois dsigitos na pagina
print('{}x{:2}={}'.format(n,2,n*2))
print('{}x{:2}={}'.format(n,3,n*3))
print('{}x{:2}={}'.format(n,4,n*4))
print('{}x{:2}={}'.format(n,5,n*5))
print('{}x{:2}={}'.format(n,6,n*6))
print('{}x{:2}={}'.format(n,7,n*7))
print('{}x{:2}={}'.format(n,8,n*8))
print('{}x{:2}={}'.format(n,9,n*9))
print('{}x{:2}={}'.format(n,10,n*10))
print('-'*12)