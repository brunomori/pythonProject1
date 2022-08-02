from datetime import date
atual=2022
nome=str(input('Olá, qual é o seu nome?'))
sexo=int(input('''Qual o seu sexo ?
[1]Masculino
[2]Feminio'''))

if sexo==1:
    print('Você é do sexo Masculino, se fudeu! deve-se se alistar {}'.format(nome))

if sexo==2:
    print('Você está dispensado, tenha um otimo dia {}'.format(nome))
    exit()

nasc = int(input('Digite o ano do nascimento:'))
idade = atual-nasc
print('Quem nasceu em {}, tem {}  anos'.format(nasc,idade))

if idade ==18:
    print('Você deve se alistar imediatamente')


elif idade < 18:
    saldo=18-idade
    ano=atual+saldo
    print('Você deve se alistar em breve, ainda faltam {} anos:'.format(saldo))
    print('Você deve se alistar em {} '.format(ano))


elif idade > 18:
    saldo=idade-18
    ano=atual-saldo
    print('Você já deveria ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))

print('Boa sorte Sr. {}'.format(nome))