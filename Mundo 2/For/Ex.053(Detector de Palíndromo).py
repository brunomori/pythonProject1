frase=str(input('Digite uma frase')).strip().upper()    #strip tira esapaço do comeco e fim
palavras = frase.split() #Dividir as palavras
junto= '*'.join(palavras) #junta as palavras
inverso= ''
for letra in range(len(junto)-1,-1,-1):
    #len lê a letra , +1 é pq o STR termina no penultima letra,
    #-1 é pq a primeira letra seria 0 mas em STR tem que ser menos um.
    #-1 para ir voltand 1 em 1

    inverso += junto[letra]
    #inver + junto
print(junto, inverso)
if junto==inverso:
    print('A palavra é igual de tras para frente!')
else:
    print('A apalvra não é igual de tras para frente')

