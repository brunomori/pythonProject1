('sortetio de alunos ')

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1,a2,a3,a4]
escolhido= random.choice(lista)
(' o aluno escolhido foi {}'.format(escolhido))


#######################################
# ('sortetio de alunos ')

#from random import choice
# a1 = input('Primeiro aluno: ')
# a2 = input('Segundo aluno: ')
# a3 = input('Terceiro aluno: ')
# a4 = input('Quarto aluno: ')
# lista = [a1,a2,a3,a4]
# escolhido= choice(lista)
#(' o aluno escolhido foi {}'.format(escolhido))


# import random
# a1 = input('Primeiro aluno: ')
# a2 = input('Segundo aluno: ')
# a3 = input('Terceiro aluno: ')
# a4 = input('Quarto aluno: ')
# print('O aluno escolhido foi {}'.format(random.choice([a1, a2, a3, a4])))