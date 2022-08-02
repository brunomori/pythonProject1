from datetime import date
n=int(input('Digite o ano de nascimento.'))
atual=date.today().year
idade=atual-n
print('Sua idade é {} '.format(idade))

if idade <=9:
    print('Você é Mirim ')

elif idade  <= 14:
    print('Você é Infantil ')

elif idade  <=19:
    print('Você é junior ')

elif idade  <= 25:
    print('Você é Senior ')

else:
    print('Você é Master  ')

