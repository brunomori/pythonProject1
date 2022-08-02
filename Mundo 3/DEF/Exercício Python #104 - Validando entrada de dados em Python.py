def leiaINt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            return f'Erro , digite um numero valido'
        if ok:
            break
    return valor

n=leiaINt('Digite um numero')
print(f'Voce acabou de digitar {n}')