import os
os.system("cls")

primeira_nota= int(input("Digite a primeira nota: "))
segunda_nota= int(input("Digite a segunda nota: "))
media= float(primeira_nota + segunda_nota) / 2

if media >= 6:   
    print("Parabéns")
    print(f"Sua média na matéria foi {media}")

elif media >=4.1 and media <= 5.9:
    print("Recuperação")
    print(f"Sua média na materia foi {media}")
else:
    print("Reprovado")
    print(f"Sua média na mmateria foi {media}")



