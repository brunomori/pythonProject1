matriz=[[0,0,0],[0,0,0],[0,0,0]]
somaPar=0
SomaColuna=0
Maior=0
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor p[{l},{c}]:'))


for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c]%2==0:
            somaPar+=matriz[l][c]
    print()

for l in range(0,3):
    SomaColuna+=matriz[l][2]

for c in range(0,3):
    if c==0:
        Maior=matriz[1][c]
    elif matriz[1][c]>Maior:
        Maior=matriz[1][c]


print(somaPar)
print(SomaColuna)
print(f'O maior numero digitado foi {Maior}')