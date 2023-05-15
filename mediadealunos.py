#!/usr/bin/python3

tamanho=2
nome = []
notas = []
for i in range(0, tamanho,1): 
   nome.append(input ("Insira o nome:"))
   notas.append(float(input("Insira a nota:")))
somatorioNotas= sum(notas) 
media= somatorioNotas/tamanho 
for j in range(0, tamanho, 1):
   if notas[j]>media:
      print("Parabéns",nome[j],"ficou com acima da média com ", notas[j])
 
print("A media eh", media) 