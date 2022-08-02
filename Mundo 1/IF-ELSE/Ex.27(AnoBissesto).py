from datetime import date
ano = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual'))
if ano == 0:
    ano= date.today().year
if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:
    print('O ano é {} é bissexto'.format(ano))
else:
    print(' o ano {} não é bissexto'.format(ano))

'''ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.

WIKI: "... ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que NÃO são múltiplos de 400)..."

Resumindo:

*... SE o ano dividido por 100 tiver o resto diferente ( != ) de 0(zero) OK, ele é BISSEXTO.

Caso o ano dividido por 100 tiver resto igual a 0(zero) negando a primeira afirmação(e colocando o "OR" em ação)...  o resto de  ano dividido por 400 também deverá ser igual a 0 para que o ano seja BISSEXTO.

* SE ano % 4 for 0(zero) E ano % 100 diferente de 0(zero) o ano será bissexto
* CASO CONTRÁRIO ano % 400 deve ser 0 para que o ano seja bissexto
'''