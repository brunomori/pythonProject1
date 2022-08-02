pessoa=dict()
galera=list()
contador=0
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome:'))
    while True:
        pessoa['sexo']=str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade']=int(input('Idade:'))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        coninuar=str(input('Deseja continua [S/N]')).upper().strip()[0]
        if coninuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if coninuar=='N':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print(f'A media da idedade de todos os integrantes é {soma/len(galera)}')
media=soma/len(galera)
print(f'As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end='')

print(f'Pessoas acima da media ')
for a in galera:
    if a['idade']>=media:
        print(f'A {a["nome"]} tem a idade a cima da media',end='')