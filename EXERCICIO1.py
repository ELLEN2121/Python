'''
Criar uma função que crie um vetor (list com 1 linha e n colunas)/matriz (list n linhas e m
colunas). Para esta função, consideramos como argumentos de entrada a quantidade de
elementos (n linhas e m colunas) e um valor padrão a ser atribuído a todos eles.
def criarMatrizPd(qtdLinhas, qtdColunas, valorPadrao)
'''
vetor = []
def criarMatrizPd(qntLinhas,qntColunas,valorPadrao):
    for i in range(qntLinhas):
        print("linha",i)
        for j in range(qntColunas):
            print("Coluna",j)
            vetor.append(valorPadrao)

    print(vetor)

qntLinhas = 4
qntColunas = 2
valorPadrao = 1
criarMatrizPd(qntLinhas,qntColunas,valorPadrao)