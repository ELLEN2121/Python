'''
c. Criar uma função que crie um vetor (list com 1 linha e n colunas)/matriz (list n linhas e m
colunas). Para esta função, consideraremos como argumentos de entrada a quantidade de
elementos (n linhas e m colunas). Os elementos de entrada são definidos randomicamente.
def criarMatrizR(qtdLinhas, qtdColunas):
'''
import random

vetor = []

def criarMatrizR(qntLinhas,qntColunas):
    for i in range (qntLinhas):
        for j in range (qntColunas):
            numero = random.random()
            vetor.append(numero)
    print(vetor)

qntLinhas = 2
qntColunas = 2
criarMatrizR(qntLinhas,qntColunas)
