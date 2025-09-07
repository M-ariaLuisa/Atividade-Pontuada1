import os
os.system("cls")

litros=float(input("Digite a quantidade de litros desejada: "))
combustivel= str(input("Digite a inicial do combustivel desejada (A/G): "))

if combustivel== "A" and litros <= 25:
    valor= litros * 3.79
    desconto= valor * 0.10
    valor_total= valor - desconto
    print(f"O valor total a ser pago é R${valor_total:.2f}")

elif combustivel== "A" and litros > 25:
    valor= litros * 3.79
    desconto= valor * 0.20
    valor_total= valor - desconto
    print(f"O valor total a ser pago é R${valor_total:.2f}")

elif combustivel== "G" and litros <= 25:
    valor= litros * 6.59
    desconto= valor * 0.15
    valor_total= valor - desconto
    print(f"O valor total a ser pago é R${valor_total:.2f}")

elif combustivel== "G" and litros > 25:
    valor= litros * 6.59
    desconto= valor * 0.30
    valor_total= valor - desconto
    print(f"O valor total a ser pago é R${valor_total:.2f}")





    