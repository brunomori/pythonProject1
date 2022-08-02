'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com
o nome "SANTO".'''

cid=str(input('Digite o nome da cidade')).strip()
c1=cid.upper()
div=c1.split()

print('SANTO'in div[0])