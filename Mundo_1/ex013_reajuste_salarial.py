#Desafio 013: Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
salario = salario + (salario * 15 / 100)

print(f'O salário de R${salario} com aumento de 15% vai passar a ser R${(salario):.2f}')
