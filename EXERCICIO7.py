'''
g. Criar uma função que calcule a média dos elementos de uma matriz
def mediaMatriz(matriz):
'''
matriz = [[2,2],[2,2]]
def mediaMatriz(matriz):
    tamanhoMatriz = len(matriz)
    for i in range(tamanhoMatriz):
        soma=sum(matriz[i])
        elementos = len(matriz[i])
        media = soma/elementos
        print("O valor da média eh ",media)

mediaMatriz(matriz)