'''
DADA DUAS MATRIZES, MULTIPLIQUE ELAS
'''
matrizUm = []
matrizDois = []
matrizResult = []

n = int(input("Insira o numero de linhas da primeira matriz"))
m = int(input("Insira o numero de colunas primeira matriz"))

for i in range (0, n, 1):
    for j in range (0,m,1):
        valor =int(input("Insira o valor: "))
        matrizUm.append(valor)
print("Matriz Um: ", matrizUm)


n = int(input("Insira o numero de linhas da primeira matriz"))
m = int(input("Insira o numero de colunas primeira matriz"))

for i in range (0, n, 1):
    for j in range (0,m,1):
        valor =int(input("Insira o valor: "))
        matrizDois.append(valor)
print("Matriz Um: ", matrizDois)


tamanhoUm = len(matrizUm)
tamanhoDois = len(matrizDois)

for i in range(tamanhoUm):
    for y in range(tamanhoDois):
        matrizResult.append(matrizUm[i]*matrizDois[y])
        print(matrizResult)