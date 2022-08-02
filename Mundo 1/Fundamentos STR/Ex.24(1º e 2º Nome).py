'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''


n=str(input('Digite seu nome copleto')).split()

print('Seu primei nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))     'o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.'