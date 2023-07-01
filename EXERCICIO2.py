'''
Criar uma função que crie um vetor (list com 1 linha e n colunas)/matriz (list n linhas e m
colunas). Para esta função, consideramos como argumentos de entrada a quantidade de
elementos (n linhas e m colunas). Os elementos de entrada são fornecidos pelo usuário.
def criarMatriz(qtdLinhas, qtdColunas):
'''
import random
vetor = []
posicaoAtual = []
posicaoMaisum = []
aux = []
vetorOrdenado = []
def criarMatriz(qntLinhas,qntColunas):
    for i in range(qntLinhas):
        for j in range(qntColunas):
            vetor.append(input("Insira um valor: "))
    return vetor

def ordena_vetor(vetor,qntLinhas,qntColunas):

    for i in range(len(vetor)):
        menor = min(vetor)
        vetorOrdenado.append(menor)
        vetor.remove(menor)

    print(vetorOrdenado)
    print("Vetor alinhado")



qntLinhas = int(input("Insira a quantidade de linhas: "))
qntColunas = int(input("Insira a quantidade de colunas: "))S
vetor = criarMatriz(qntLinhas,qntColunas)
ordena_vetor(vetor,qntLinhas,qntColunas)
