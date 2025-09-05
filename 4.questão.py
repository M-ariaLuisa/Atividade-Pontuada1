import os
os.system("cls")

print(f"""
    Fruta	Até 5 Kg	Acima de 5 Kg
    Morango	R$ 2,50 por Kg	R$ 2,20 por Kg
    Maçã	R$ 1,80 por Kg	R$ 1,50 por Kg
      """)

kg= float(input("Digite a quantidade de kg desejada:"))
valor= float(input("Digite o valor pago:"))

if kg>= 10 or valor>= 15:
    resultado= valor - (valor * 0.10)
    print(f"Comprou {kg} kg e gastou {resultado} reais")

else:
    print(f"Comprou {kg} e gastou {valor}")
