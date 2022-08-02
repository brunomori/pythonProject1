#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
#=======================================================================================

nome= str(input('Digite seu nome completo')).strip()

nome=str(input('Digite seu nome')).strip()

print('Seu nome em Maiúsculo é {}'.format(nome.upper()))
print('Seu nome em Minusculo é {}'.format(nome.lower()))
print('O seu nome tem {} leras'.format(len(nome)-nome.count(' ')))  #verificar os espaços entre as lestras , assim, tirando os espaços só sobra as letras!
#tudo o que for .conut(' ')   ele vai falar quantos tem
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #encontre no primeiro espaço
separa = nome.split()  #Cria lista
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
print('Seu segundo nome é {} e ele tem {} letras'.format(separa[1],len([1])))
