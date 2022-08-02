def voto (ano):
    from datetime import  date
    atual=date.today().year
    idade=atual-ano
    if idade <16:
        return f' Com {idade} anos, não vota'
    elif idade>16 <18 or idade>65:
        return f'Pessoas com {idade} não é obrigado a vota'
    else:
        return f' Pessoas com {idade} são obrigadas a vota'


ano=int(input('Digite sua data de nasicmento'))
print(voto(ano))