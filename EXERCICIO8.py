'''
h. Criar uma função que encontre o maior elemento de uma matriz.
def maiorMatriz(matriz):
'''

matriz = [[250,31],[100,0]]
valoresMax = []
def maiorMatriz(matriz):
    tamanhoMatriz = len(matriz)
    for i in range(tamanhoMatriz):
        vlrMax = max(matriz[i])
        valoresMax.append(vlrMax)
    valorMaxMatriz = max(valoresMax)
    print(valorMaxMatriz)
maiorMatriz(matriz)
