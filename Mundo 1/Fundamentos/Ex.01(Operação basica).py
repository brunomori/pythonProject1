print('\033[1:97:40m Olá esse é meu primeiro programa, ele irar:\033[m \033[0:31:44mSomar\033[m,Multiplicar, Dividir, Fazer a media e depois exibir seu cadastro')
n1=int(input('Digite o primeiro  o numero!'))
n2=int(input('Ok, digite o segundo numero'))

s=n1+n2
m=n1*n2
d=n1/n2
x=s/2

print('mAgora vamos fazer seu cadastro...')
i1=input('Digite seu peso')
i2=input('digite sua altura')
i3=input('digite seu nome')
i4=input('digite sua data de nascimento')


print('Analisando seu dados ...... xD já sei tudo!')
print('A parte mais chata primeiro!\n A soma ficou:{}\n a multiplicação ficou:{}\n a divisão ficou:{}\n a media ficou{}\n'.format(s,m,d,x))
print('Ahhh, deu certo né? Agora a segunda parte...\n O seu peso é:{}\n a sua altura é:{}\n seu nome é:{}\n seu nascimento é:{}'.format(i1,i2,i3,i4))


print('Vamos para a segunda parte?')
M=input('digite algo')
print(f'A sua resposta é feita só de números? {M.isnumeric()}')
print(f'A sua resposta é feita só de letras? {M.isalpha()}')
print(f'A sua resposta contém só letras e números? {M.isalnum()}')
print(f'A sua resposta contém só espaços? {M.isspace()}')



#input armazernar informação   // .format() para colocar dentro as informaçoes e printa na tela
#int (numeros inteiro 1/2/3/-4)
#float (numeros real 1.75/15.00)
#bool True / False
#str  'Olá'(escria)

