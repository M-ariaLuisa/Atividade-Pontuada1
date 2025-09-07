import os
os.system("cls")

print(f"""
    Fruta	Até 5 Kg	Acima de 5 Kg
    Morango	R$ 2,50 por Kg	R$ 2,20 por Kg
    Maçã	R$ 1,80 por Kg	R$ 1,50 por Kg
      """)

morango= float(input("Informe a quantidade de morango desejada (kg):"))
maca= float(input("Informe a quantidade de maçã desejada (kg): "))

if morango <=5:
    preco_morango= morango * 2.5

else:
    preco_morango= morango * 2.2

if maca<= 5:
    preco_maca= maca * 1.8

else:
    preco_maca= maca * 1.5

peso_total= morango + maca
valor_total= preco_morango + preco_maca

if peso_total >= 10 or valor_total > 15:
    valor_com_desconto= valor_total - (valor_total * 0.10) 
    print(f"Foram adquiridos {morango}kg de morango e {maca}kg de maçã e o total a ser pago é R${valor_com_desconto:.2f} ")

else:
    print(f"Foram adquiridos {morango}kg de morango e {maca}kg de maçã e o total a ser pago é R${valor_total:.2f} ")





