expressão=str(input('Digitea expressão:'))

expressãoD=0
expressãoE=0

for simbolo in expressão:
    if simbolo=='(':
        expressãoE+=1
    if simbolo==')':
        expressãoD+=1

if expressãoE==expressãoD:
    print('A expressão é valida')
else:
    print('A expressão não é valida')

