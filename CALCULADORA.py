modo=0
modo=int(input(("\nMENU:\n[1]DIVISÃO\n[2]SOMA\n[3]MULTIPLICAÇÃO\n[4]SUBTRAÇÃO\n[5]EXPONENCIAL\n")))
while (modo==1):
        tabuada=int(input("Digite um número para exibir a tabuada:\n"))
        print("tabuada do número ", tabuada)
        for valor in range(1,11,1):
            print(str(tabuada)+"/"+str(valor)+"="+str(tabuada/valor))

        resp=input("DESEJA SAIR?").upper()
        if resp=="NAO":
            continue
        else:
            break


while (modo==2):
        tabuada=int(input("Digite um número para exibir a tabuada:\n"))
        print("tabuada do número ", tabuada)
        for valor in range(0,11,1):
            print(str(tabuada)+"+"+str(valor)+"="+str(valor+tabuada))

        resp = input("DESEJA SAIR?").upper()
        if resp == "NAO":
            continue
        else:
            break

while (modo==3):
        tabuada=int(input("Digite um número para exibir a tabuada:\n"))
        print("tabuada do número ", tabuada)
        for valor in range(0,11,1):
            print(str(tabuada)+"*"+str(valor)+"="+str(valor*tabuada))
        resp = input("DESEJA SAIR?").upper()
        if resp == "NAO":
            continue
        else:
            break

while (modo==4):
        tabuada=int(input("Digite um número para exibir a tabuada:\n"))
        print("tabuada do número ", tabuada)
        for valor in range(0,11,1):
            print(str(tabuada)+"-"+str(valor)+"="+str(valor-tabuada))
        resp = input("DESEJA SAIR?").upper()
        if resp == "NAO":
            continue
        else:
            break

while (modo==5):
        tabuada=int(input("Digite um número para exibir a tabuada:\n"))
        print("tabuada do número ", tabuada)
        for valor in range(0,11,1):
            print(str(tabuada)+"^"+str(valor)+"="+str(valor**tabuada))

        resp = input("DESEJA SAIR?").upper()
        if resp == "NAO":
            continue
        else:
            break
