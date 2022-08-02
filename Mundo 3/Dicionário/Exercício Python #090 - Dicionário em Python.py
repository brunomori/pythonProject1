aluno={}
aluno['nome']=str(input('Nome:'))
aluno['media']=float(input(f'A media do aluno {aluno["nome"]}:'))

if aluno['media']<=3:
    aluno['situação']='reprovado'

elif aluno['media']<=5:
    aluno['situação']='recuperação'
else:
    aluno['situação']='aprovado'

print('-='*30)
for chave,valor in aluno.items():   #graças a função .items , o for vai recerber na 1 variavel: as chaves.
    #2 variavel valores  (O que é chave até os dois pontos, depois é o valor.? aluno_1={"nome":bruno)
    print(f'{chave} é igual a {valor}')
print('-='*30)





