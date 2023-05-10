import main

def soma_com_sinal_e_magnitude(a_bin, b_bin):
    # Verifica os sinais dos números
    a_sinal = a_bin[0]
    b_sinal = b_bin[0]

    # Remove os sinais dos números
    a_mag = a_bin[1:]
    b_mag = b_bin[1:]

    # Realiza a operação de soma
    resultado_mag = bin(int(a_mag, 2) + int(b_mag, 2))[2:]

    # Verifica o sinal do resultado
    resultado_sinal = a_sinal

    # Verifica se ocorreu carry-out (estouro) na soma
    if len(resultado_mag) > len(a_mag):
        resultado_sinal = '1' if resultado_sinal == '0' else '0'
        resultado_mag = resultado_mag[1:]

    # Adiciona o sinal ao resultado
    resultado_bin = resultado_sinal + resultado_mag

    return resultado_bin


def subtracao_com_sinal_e_magnitude(a_bin, b_bin):
    # Verifica os sinais dos números
    a_sinal = a_bin[0]
    b_sinal = b_bin[0]

    # Remove os sinais dos números
    a_mag = a_bin[1:]
    b_mag = b_bin[1:]

    # Realiza a operação de subtração
    resultado_mag = bin(int(a_mag, 2) - int(b_mag, 2))[2:]

    # Verifica o sinal do resultado
    resultado_sinal = a_sinal

    # Verifica se ocorreu carry-out (estouro) na subtração
    if resultado_mag[0] == '-':
        resultado_sinal = '1' if resultado_sinal == '0' else '0'
        resultado_mag = resultado_mag[1:]

    # Adiciona o sinal ao resultado
    resultado_bin = resultado_sinal + resultado_mag

    return resultado_bin


def complemento_dois(numero_bin):
    # Inverte os bits
    complemento = ''.join('1' if bit == '0' else '0' for bit in numero_bin)

    # Adiciona 1
    resultado = bin(int(complemento, 2) + 1)[2:].zfill(len(numero_bin))

    return resultado

def soma_complemento_dois(a_bin, b_bin):
    a_comp = complemento_dois(a_bin)
    b_comp = complemento_dois(b_bin)
    resultado_comp = bin(int(a_comp, 2) + int(b_comp, 2))[2:].zfill(max(len(a_bin), len(b_bin)))
    resultado = complemento_dois(resultado_comp)

    return resultado


def subtracao_complemento_dois(a_bin, b_bin):
    # Calcula o complemento de dois de b
    b_comp = complemento_dois(b_bin)

    # Realiza a soma entre a e -b
    resultado_bin = bin(int(a_bin, 2) + int(b_comp, 2))[2:].zfill(max(len(a_bin), len(b_bin)))

    # Verifica se ocorreu um estouro (carry-out)
    if len(resultado_bin) > len(a_bin):
        resultado_bin = resultado_bin[1:]

    return resultado_bin

def resultados(resultado_bin):
    resultado_dec = main.binario_para_decimal(resultado_bin)

    print("Resultado (Base 2):", resultado_bin)
    print("Resultado (Base 10):", resultado_dec)


with open('C:\\Users\\ELLEN M S CALDAS\\PycharmProjects\FAC_Trabalho01\\entrada', "r") as arquivo:
    # Lê o primeiro número e converte para inteiro
    numero1 = arquivo.readline().strip()

    # Lê o segundo número e converte para inteiro
    numero2 = arquivo.readline().strip()
resultado_subtracao_bin = subtracao_com_sinal_e_magnitude(numero1,numero2)
resultado_soma_bin = soma_com_sinal_e_magnitude(numero1,numero2)
print("\n")
print("---------- SOMA E SUBTRAÇÃO SINAL E MAGNETUDE -----------")
print("Soma : ",soma_com_sinal_e_magnitude(numero1,numero2).zfill(32))
print("Subtração : ", subtracao_com_sinal_e_magnitude(numero1,numero2).zfill(32))
resultados(resultado_soma_bin)
resultados(resultado_subtracao_bin)
print("---------- SOMA E SUBTRAÇÃO COMPLEMENTA DOIS -----------")
print("Soma : ",soma_complemento_dois(numero1,numero2).zfill(32))
print("Subtração : ", subtracao_complemento_dois(numero1,numero2).zfill(32))
resultados(soma_complemento_dois(numero1,numero2))
resultados(subtracao_complemento_dois(numero1,numero2))


