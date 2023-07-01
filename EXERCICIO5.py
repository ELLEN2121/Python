'''
e. Criando uma matriz com valores de uma string. De forma similar à função anterior,
criaremos outra função, agora para uma matriz. Neste caso, separaremos os elementos de
cada coluna com a vírgula (“,”) e cada linha com um ponto-e-vírgula (“;”). Dica: neste caso, a
lógica é muito parecida com o vetor (exercício e), mas primeiro deveremos dividir as linhas
e, para cada linha, teremos que dividir as colunas.
'''

linhas = []
colunas = []
valoresLinhas = []
valoresColunas = []
valores = []
valoresDois= []

tipo = int(input("Insira o tipo das variaveis: [1] Int [2]Float [3] String"))
valores.append(input("Insira os valores das variaveis, separadamente por VIRGULA (,) e coluna por (;) : "))

qntLinhas = valores[0].count(',')
qntColunas = valores[0].count(';')


valoresDois = valores[0].strip(",;")



qntLinhas = len(valoresLinhas)
valoresLinhas = valores[0].split(';,')
qntColunas = len(valoresColunas)
if (tipo==1):
    for i in range(valoresLinhas):
        for y in range(valoresColunas):
           valor  =  int(valores[valoresLinhas][valoresColunas])
           valoresDois.append(valor)

