import os
os.system("cls")

renda_mensal= float(input("Informe o valor da sua renda mensal: "))
valor_desejado= float(input("Digite o valor de empréstimo desejado: "))
prestacao= int(input('Quantas prestações?'))

total_emprestimo= renda_mensal *10
valor_prestacao= valor_desejado / prestacao
valor_prestacao_ajustado= (renda_mensal * (30/100))

if (valor_desejado <= total_emprestimo) and (valor_prestacao <= valor_prestacao_ajustado):
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi reprovado')