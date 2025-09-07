import os
os.system("cls")

nome= str(input("Digite o seu nome:"))
sexo= str(input("Informe o seu sexo: F/M: "))
estado_civil= str(input("Informe o seu estado civil: "))

if estado_civil== "CASADA" and sexo== "F" :
  tempo_de_casada= int(input("Informe a quanto tempo a senhora está casada: "))

  print(f""""
    Nome:{nome}
    Sexo:{sexo}
    Estado civil: {estado_civil}
    Tempo de casada: {tempo_de_casada}
     """)

else:
  print(f""""
    Nome:{nome}
    Sexo:{sexo}
    Estado civil: {estado_civil}
     """)

  
