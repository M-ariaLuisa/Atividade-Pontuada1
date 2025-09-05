import os
os.system("cls")

litros=float(input("Digite a quantidade de litros desejada"))
combustivel= str(input("Digite a inicial do combustivel desejada: A/G"))

if combustivel== "A" and litros <= 25:
    