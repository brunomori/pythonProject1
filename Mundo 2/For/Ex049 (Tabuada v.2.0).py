print('Bem vindo ao programa de tabuada!')
nome=str(input('Qual é o seu nome ?'))
sexo=int(input('''Qual é o seu sexo?
[1]Masculino
[2]Feminino'''))

if sexo==1:
    print('Seja bem vinda SENHOR {}'.format(nome))
    n=int(input('Digite um numero para saber sua tabuada!'))
    for lista in range (0,10):
        print('{}x{}={}'.format(n,lista,n*lista))

if sexo==2:
    print('Seja bem vindo SENHORITA {}'.format(nome))
    n=int(input('Digite o numero para saber sua tabuada'))
    for lista in range (0,10):
        print('{}x{}={}'.format(n,lista,n*lista))

print('Obrigado volte sempre')