'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome'''

n=str(input('Digite o nome de uma pessoa')).strip()

print('Seu nome tem Silva ?{}'.format('SILVA' in n.upper()))


