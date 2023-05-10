decimal=[]
valor = []
bits = 8
# Binario para decimal
def binario_para_decimal(binario):

    decimal = 0
    for bit in binario: # verifica se o bit é 0 ou 1
        decimal = decimal * 2 + int(bit)
    return decimal

#Decimal para binario
def decimal_para_binario(decimal):
    if decimal == 0:
        return '0'

    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2

    return binario

# Sinal e magnitude para decimal
def sinal_magnitude_para_decimal(valor):

    sinal = int(valor[0]) #primeiro item referente ao sinal
    magnitude = binario_para_decimal(valor[1:]) #complemento
    return (-1)**sinal * magnitude

# Complementa Dois para decimal
def complemento_de_2_para_decimal(valor):
    sinal = int(valor[0]) # Binario na posição 1 do vetor é 0 ou 1
    if sinal == 1:
        complemento = ''.join(['1' if bit == '0' else '0' for bit in valor[1:]]) # verifica o complemento apos o sinal
        magnitude = binario_para_decimal(complemento) + 1 # soma mais um pq é negativo
        return -magnitude
    else:
        return binario_para_decimal(valor[1:])





# abre o arquivo e lê o conteúdo
with open('C:\\Users\\ELLEN M S CALDAS\\PycharmProjects\FAC_Trabalho01\\entrada', 'r') as arquivo:
    conteudo = arquivo.read()


# divide o conteúdo em linhas
linhasArquivo = conteudo.splitlines()

for linha in linhasArquivo:

    print("--------------Conversão -------------\n")
    print("Numero em Binario: ", linha)
    print("Binario em Decimal: ", binario_para_decimal(linha))
    print("Complementa Dois em Decimal: ", complemento_de_2_para_decimal(linha))
   # print("Complementa Dois em Binario: ", decimal_para_binario(binario_para_decimal(linha)))
    print("Sinal e Magnetude em Decimal:", sinal_magnitude_para_decimal(linha))






'''
with open("C:\\Users\\ELLEN M S CALDAS\\PycharmProjects\\FAC_Trabalho01\\saida.txt", "w") as escreverArquivo:
        escreverArquivo.write("Numero em Binario: ", linha, "\n")
        escreverArquivo.write("--------------Conversão -------------\n")
        escreverArquivo.write("Binario ---->  Decimal: ", binario_para_decimal(linha))
        escreverArquivo.write("Complementa dois ----> Decimal: ", complemento_de_2_para_decimal(linha))
        escreverArquivo.write("\n")
'''