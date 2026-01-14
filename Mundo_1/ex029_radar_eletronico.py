#Desafio 029: Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual é a velocidade do veículo em Km/h? '))

if (v <= 80):
    print('Você está dentro do limite de velocidade :)')
else:
    print(f'Você foi multado! Sua multa é de R${(v - 80) * 7}')
