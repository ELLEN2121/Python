#!/usr/bin/python3
#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br

dividendo = int(input("Digite um numero (Base decimal) para ser convertido em Binário: "))
numero_digitado = dividendo
quociente = 1
lista = []

while quociente >= 1:
  resto = dividendo%2 #pega o resto 
  lista.insert(0,resto)
  quociente = dividendo // 2 #pega o inteiro 
  dividendo = quociente # o dividendo vira o quociente 
  
#binario = ''.join([str(item) for item in lista])
print("O número",numero_digitado,", quando convertido em binário, vale:",lista)