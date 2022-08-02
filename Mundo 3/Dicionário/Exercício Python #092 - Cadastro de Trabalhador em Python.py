from datetime import  datetime
lista={}
lista['Nome']=str(input('Nome:'))
ano=int(input('Ano de nascimento'))
lista['Carteira']=int(input('Carteira de trabalho (0 não tem)'))
lista['Idade']=datetime.now().year-ano
if lista['Carteira']!=0:
    lista['Ano da contratação']=int(input('Ano de Contratação'))
    lista['Salario']=float(input('Salario:'))
    lista['Aposentadoria']=lista['Idade']+((lista['Ano da contratação']+35)- datetime.now().year)

for chave,valor in lista.items():
    print(f'{chave}:{valor}')