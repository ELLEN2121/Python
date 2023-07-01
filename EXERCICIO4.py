'''
d. Criando um vetor com valores de uma string. Quando fazemos a entrada de dados de um
vetor lendo o valor de cada elemento, são feitas várias entradas do usuário. Em termos
práticos, é uma tarefa enfadonha para o usuário fazer várias entradas. Podemos oferecer a
possibilidade do usuário fornecer todos os valores a partir de uma única entrada,
estabelecendo para isso um padrão. Em nosso caso, separaremos os elementos com um
caractere específico, a vírgula “,”. Neste caso, todos os elementos serão fornecidos em uma
string, obtida em um único input, que precisará ser tratada para preencher o vetor. Nossa
função criará um novo vetor contendo os elementos passados na string de entrada valores,
convertendo os valores conforme o tipo, passado como segundo argumento
def preencherVetor(valores, tipo):
'''
valores = []

def preencherVetor(valores, tipo):
    valoresDois = []
    posicaoVetor = len(valores)
    numerosVetores = valores[posicaoVetor-1]
    if(tipo==1):
        numerosInternos = len(numerosVetores)
        for i in range(numerosInternos):
            valoresz = int(numerosVetores[i])
            valoresDois.append(valoresz)
        print(valoresDois)

    elif(tipo==2):
        numerosInternos = len(numerosVetores)
        for i in range(numerosInternos):
            valoresz = float(numerosVetores[i])
            valoresDois.append(valoresz)
        print(valoresDois)
    else:
        print(numerosVetores)

tipo = int(input("Insira o tipo das variaveis: [1] Int [2]Float [3] String"))
valores.append(input("Insira os valores das variaveis, separadamente por VIRGULA (,): ").split(','))

preencherVetor(valores,tipo)

