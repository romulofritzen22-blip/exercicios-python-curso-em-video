#Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Quanto é o salário do funcionário? R$'))

if salario > 1250:
    print(f'O salário de R${salario} com 10% de aumento será de R${salario * 1.1:.2f}')
else:
    print(f'O salário de R${salario} com 15% de aumento será de R${salario * 1.15 :.2f}')
