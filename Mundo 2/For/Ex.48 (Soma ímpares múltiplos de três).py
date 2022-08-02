soma=0
contador=0

soma1=0
contador1=0

for lista in range(1,501):
    if lista %2 ==1:
       if lista %3 ==0:
        soma = soma+lista
        contador=contador+1
    else:
        if lista % 3 == 0:
            soma1 = soma1 + lista
            contador1 = contador1+1
print('A soma de todos os valores impar é {} e eles foram somados {} vezes\nA soma de todos os valores par é {} e eles foram somados {} vezes '.format(soma,contador,soma1,contador1))



