import os
os.system("cls")

nome= str(input("Digite o nome do produto: "))
quantidade= int(input("Digite a quantidade adquirida: "))
preço= float(input("Informe o preço unitário do produto: "))
total= preço * quantidade

if quantidade <= 5:
    desconto= total * 0.02
    preco_com_desconto= total - desconto
    print(f"O desconto foi de R${desconto:.2f} e o total a pagar é {preco_com_desconto:.2f}")


elif quantidade > 5 and quantidade <= 10:
    desconto= total * 0.03
    preco_com_desconto= total - desconto
    print(f"O desconto foi de R${desconto:.2f} e o total a pagar é {preco_com_desconto:.2f}")


else:
    desconto= total * 0.05
    preco_com_desconto= total - desconto
    print(f"O desconto foi de R${desconto:.2f} e o total a pagar é {preco_com_desconto:.2f}")

    


