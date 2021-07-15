equipamentos = []
valores = []
departamentos = []
responsavel =[]
resp = "S"

while resp == "S":
        equipamentos.append(input("Equipamento: "))
        valores.append(float(input("Valor: ")))
        departamentos.append(input("Departamento: "))
        responsavel.append(input("Responsavel:"))
        resp = input("Digite S para continuar: ").upper()


busca = input("Digite o nome do equipamento: ")
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
            print("Equipamento..: ", (indice+1))
            print("Nome.........: ", equipamentos[indice])
            print("Valor........: ", valores[indice])
            print("Departamento.: ", departamentos[indice])
            print("Responsavel..: ", responsavel[indice])
