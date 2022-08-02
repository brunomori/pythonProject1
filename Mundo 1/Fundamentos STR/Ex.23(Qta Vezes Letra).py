'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e
em que posição ela aparece a última vez.'''

frase= str(input('Digite uma frase')).upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print(' A letra a aparece na posição {}'.format(frase.find('A')+1))  # find = que posição a letra a foi encontrada a primeira vez
print('A letra A aparece na posição {}'.format(frase.rfind('A')+1))  # rfind = que posição da  direita  a letra a foi encontrada a primeira vez