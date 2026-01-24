#Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço formal 
#Em 3x ou mais no cartão: 20% de juros

compras = float(input('Valor total das compras: R$'))

print('Qual vai ser a forma de pagamento?\n'
'1. PIX, dinheiro ou cheque.\n'
'2. À vista no cartão.\n'
'3. Em até 2x no cartão.\n'
'4. 3x ou mais no cartão.\n')
pagamento = int(input('Pagamento: '))

if pagamento == 1:
    print(f'Preço final: R${compras * 0.9:.2f}')
elif pagamento == 2:
    print(f'Preço final: R${compras * 0.95:.2f}')
elif pagamento == 3:
    print(f'Preço final: 2 parcelas de R${compras / 2:.2f}. Total: R${compras}.')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print(f'Preço final: {parcelas} parcelas de R${compras * 1.2 / parcelas:.2f}. Total: R${compras * 1.2:.2f}.')
else:
    print('ERRO! Selecione uma forma de pagamento válida.')
