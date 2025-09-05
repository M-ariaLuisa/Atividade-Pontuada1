import os
os.system("cls")

cor = str(input("Digite a cor do produto desejado: "))

match cor:
    case "verde":
        print("Custa R$ 10,00")

    case "azul": 
        print("Custa R$ 20,00")

    case "amarelo":
        print("Custa R$ 30,00")

    case "vermelho":
        print("Custa R$ 40,00")
   
