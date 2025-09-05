import os
os.system("cls")

nome= str(input("Digite o nome do produto: "))
quantidade= int(input("Digite a quantidade adquirida: "))
preço= int(input)("Digite o preço unitário: ")
total= preço * quantidade

if quantidade <= 5:
    desconto= preço * 0.2
    preco_com_desconto= preço - desconto


elif quantidade > 5 and quantidade <= 10:
    desconto= preço * 0.3
    preco_com_desconto= preço - desconto

elif quantidade > 10:
    desconto= preço * 0.5
    preco_com_desconto= preço - desconto

else:
   print(f"Não tem desconto. O valor é {total}")

    


