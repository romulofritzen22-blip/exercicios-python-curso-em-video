#Desafio 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for c in range(1, 6):
    Kg = float(input(f'Digite o peso da pessoa {c} em Kg: '))
    pesos.append(Kg)

print(f'O menor peso foi de {min(pesos):.1f}Kg e o maior peso foi de {max(pesos):.1f}Kg.')
