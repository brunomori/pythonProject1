num = cont = soma = 0
while num !=999:
    num=int(input('Digite um numero[999 para parar]:'))
    soma= soma+num
    cont=+1
print('Você digitou {} vezes e a soma entre eles foi {}'.format(cont,soma-999))
