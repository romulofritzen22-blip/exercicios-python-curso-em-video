#Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? R$'))
salário = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em até quantos anos você pretende pagar o empréstimo? '))

parcelas = casa / (anos * 12)
print(f'As parcelas mensais seriam de R${parcelas:.2f}')

if parcelas > salário * 0.3:
    print(f'Elas excedem 30% de R${salário:.2f}, portanto seu empréstimo foi NEGADO.')
else:
    print('Seu empréstimo foi APROVADO!')
