frase= 'Curso em video python'


print(frase [3])           #Vai p/ o 3 carater
print(frase [13])          #Vai p/ o 13 carater
print(frase[1])            #Vai para o primeiro carater, mas começa no zero
print(frase[3:13])         #Do 3 carater ate 12 carater
print(frase[1:15:2])       #Primeiro caracter ate o 14 carater, pulando dois em dois( da casa 1 até a 15 dois em dois)
print(frase[:5])           #Começa do 0 ate o caracter o 4 (pois não tem começo, vira zero)
print((frase[15:'fim']))   #Começa da casa 15 ate o fim, pois nao tem ó numero no último campo
print(frase[9:'fim':3])    #Vai começar na casa 9 e vai ate o final, pois não tem numero, e vai a pular 3 em 3
print(frase.split())       #Divide a frase
print(dividido[0])         #Divide a frase
print(dividido [2 [3]])    #Pega video e mostra a letra 3
len(frase)                 #Ler quantos caracteres tem dentro na frase
frase.count('o')           #Contar quantas letras 'o' tem na da frase
frase.count('o',0,13)      #Considerar do 0 ate o 13 (na, verdade ate o 12 e vai procurar quantos o tem e printar)
frase.find('deo')          #Vai encontrar quantas  posição do a
frase.find('Android')      #Vai retornar -1, siginifica que não existe
curso' in frase            #Vai escrever se existe a palavra 'curso',se existe vai printar: true
#frase.reaplace'pyton','Android' #Vai trocar todas as palvaras pyton,por Android
#frase.upper{}              #Vai deixa a a frase com letra maiscula
#frase.lower{}              #Vai deixar a  frase Minuscula
#frase.capitalize{}         #Vai jogar tudo p/ minusculo menos o primeiro que vai p/ Maisculo
#frase.title{}              #Vai fazer capitalize palavra por palavra atravez dos espaços
#frase .strip{}              #Vai remover os espaços vazios do começo e do fim/ coloca-se na declaração da variavel
#frase.rstrip{}             #Vai remover os ultimos espaços (direita)
#frase.lstrip{}             #Vai remover os primeiros espaços (esquerda)
#frase.split{}              #Vai ocorrer divisão entre os espaços das palavras, fazendo cada palavra começar do zero e acabar no fime dela.
#'-'.join(frase)            #juntar os elementos e colocar o tracinho
