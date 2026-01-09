#Desafio 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kilômetros você percorreu com o carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))

preço = (km * 0.15) + (dias * 60)

print(f'Com {dias} dias alugados e {km} kilômetros rodados você terá que pagar R${preço:.2f}')
