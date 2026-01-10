#Desafio 012: Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Qual é o valor do produto? R$'))
valor_final = valor - (valor * 5 / 100)

print(f'O produto de R${valor} com 5% de desconto vai custar R${valor_final:.2f}')
