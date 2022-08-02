def ajuda(com):
    help(com)

def titulo(msg,cor=0):
    tam=len(msg)
    print('-'*tam)
    print(msg)
    print('-'*tam)

comando=''
while True:
    titulo('Sistema de ajuda Pyhelp')
    comando=str(input('Função ou Biblioteca'))
    if comando.upper()=='Fim':
        break
    else:
        ajuda(comado)
titulo('Até logo!')

