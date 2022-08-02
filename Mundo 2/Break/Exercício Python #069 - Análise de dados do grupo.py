mais18=0
cadastroH=0
mulherMenor=0
continuar=''
while True:
    print('---'*20)
    print('CADASTRE UMA PESSOA')
    print('---'*20)
    idade=int(input('Idade:'))
    sexo=str(input('Sexo [M/F]')).strip().upper()
    if sexo=='M':
        cadastroH+=1
    if idade >18:
        mais18+=1
    if sexo =='F' and idade <20:
        mulherMenor+=1
    continuar=str(input('Deseja continuar')).upper().strip()
    if continuar=='S':
        print('Vamos continuar!')
    else:
        break


print(f'Fim dos cadastros, existe {cadastroH} homem(s) cadastrado\nExiste {cadastroH} pessoas maiores de idade\nExiste {mulherMenor} mulheres com  menos de 20 anos')