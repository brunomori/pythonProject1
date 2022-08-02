ultimos=''
cinco=5
lista='Corinthians','Atlético-MG','São Paulo','Botafogo','Santos','Coritiba','Avaí','América-MG','Palmeiras','Bragantino'

print('='*15)
print(f'Lista do brasileirão{lista}')
print(f'Os cinco primeiros são {lista[0:5]}')
print(f'Os quatros ultimos são {lista[-4:]}')
print(f'Time em ordem alfabetica:{sorted(lista)}')
print(f'O Botafogo está na posição {lista.index("Botafogo")+1} posição')