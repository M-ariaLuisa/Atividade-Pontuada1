import os
os.system("cls")

A = int(input ("Digite o  primeiro numero: "))
B = int(input ("Digite o segundo numero: "))
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