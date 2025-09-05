import os
os.system("cls")

nome= str(input("Digite o seu nome:"))
sexo= str(input("Digite a inicial do seu sexo: "))
estado_civil= str(input("Digite o seu estado civil: "))

if estado_civil== "casada" and sexo== "F":
  tempo_de_casada= int(input("Digite a quanto tempo o senhor(a) está casado: "))

print(f""""
    Nome:{nome}
    Sexo:{sexo}
    Estado civil: {estado_civil}
    Tempo de casada: {tempo_de_casada}
     """)

  
