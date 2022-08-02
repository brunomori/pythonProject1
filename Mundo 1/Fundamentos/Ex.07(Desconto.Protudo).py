#print('Calculadora de desconto em %')
#pro=float(input('Digte o Valor do produto'))
#por=float(input('Digite o Valor de desconto em %'))
#des=por/100
#des= pro*des
#final=des1-pro

#print('Valor original{}'.format(pro))
#print(('valor em %  de desconto foi {}'.format(pro))
#print('valor do desconto{}'.format(des))
#print('Valor final {}'.format(final))


# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto que será concedido
desconto = float( input("Desconto (em %) para esse produto: ") )

# Transformando a porcentagem em número decimal
desconto = desconto / 100

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_original * desconto)
print('Valor com desconto: R$', valor_original * (1-desconto) )



