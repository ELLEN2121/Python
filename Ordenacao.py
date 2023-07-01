'''
Ordene um vetor e retire caso tenha repetição de numero
Ordene um vetor e retire caso tenha repetição de numero
'''
vetor = [0,0,3,5,5,9]
vetorOrdenado = []
vetorSemRep=[]

def ordenaVetor(vetor):
    tamanhoVetor = len(vetor)
    for i in range(tamanhoVetor):
        numero = min(vetor)
        vetorOrdenado.append(numero)
        vetor.remove(numero)

    print("Vetor Ordenado: ",vetorOrdenado)


def retiraRepeticao(vetor):
    tamanhoVetor = len(vetor)
    for i in range(tamanhoVetor):
        qnt = vetor.count(vetor[i])
        if(qnt>1):
            print("Numero Repetido! ", vetor[i])
            vetorSemRep.append(vetor[i])
            vetor.remove(vetor[i])
            retiraRepeticao(vetor)
        else:
            if(vetor[i] not in vetorSemRep):
                vetorSemRep.append(vetor[i])
    print("Vetor sem repetição", vetorSemRep)
    ordenaVetor(vetorSemRep)

print("Vetor Inicial: ", vetor)
retiraRepeticao(vetor)