import os
os.system("cls")

A = float(input ("Digite o  primeiro numero: "))
B = float(input ("Digite o segundo numero: "))
operacao = (input("Digite o caractere da operação desejada: + - * / "))

match operacao:
    case "+":
        resultado= A + B
        print(f"O resultado da sua operação é {resultado}")
    case "-":
        resultado= A - B
        print(f"O resultado da sua operação é {resultado}") 
    case "*":
        resultado= A * B
        print(f"O resultado da sua operação é {resultado}")
    case "/":
        resultado= A / B
        print(f"O resultado da sua operação é {resultado}")       

    case _:
        print("Opção invalida")