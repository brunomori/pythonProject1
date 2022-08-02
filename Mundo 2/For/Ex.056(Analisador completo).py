#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
IdadeHomem=0
HomemMaisVelho=''
MulherMenor=0
SomaIdade=0

for y in range (1,5):
    print('Dados da {}º Pessoa:'.format(y))
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    sexo=str(input('Sexo'))
    SomaIdade+=idade

    if y==1 and sexo=='M':
        IdadeHomem=idade
        HomemMaisVelho=nome

    if idade>IdadeHomem and sexo=='M':
        IdadeHomem=idade
        HomemMaisVelho=nome

    if idade <18 and sexo=='F':
        MulherMenor+=1




media=SomaIdade/4
print('A idade média do grupo é {}'.format(media))
print('O nome do Homem mais velho é {}, ele tem {} anos'.format(HomemMaisVelho,IdadeHomem))
print('Existe {} Mulheres menores de idade'.format(MulherMenor))




