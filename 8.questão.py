import os
os.system("cls")

cor = str(input("Digite a cor do produto desejado (Verde, Azul, Amarelo ou Vermelho): "))

match cor:
    case "Verde":
        print("Custa R$ 10,00")

    case "Azul": 
        print("Custa R$ 20,00")

    case "Amarelo":
        print("Custa R$ 30,00")

    case "Vermelho":
        print("Custa R$ 40,00")
   
