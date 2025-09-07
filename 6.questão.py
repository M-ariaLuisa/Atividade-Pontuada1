import os
os.system("cls")

primeira_nota= float(input("Digite a primeira nota: "))
segunda_nota= float(input("Digite a segunda nota: "))
media= float(primeira_nota + segunda_nota) / 2

if media >= 6:   
    print("Parabéns, você foi aprovado!")
    print(f"Sua média na matéria foi {media:.2f}")

elif media >=4.1 and media <= 5.9:
    print("Você está em recuperação.")
    print(f"Sua média na materia foi {media:.2f}")
else:
    print("Você foi reprovado.")
    print(f"Sua média na materia foi {media:.2f}")



