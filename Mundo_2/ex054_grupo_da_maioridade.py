#Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for c in range(1,8):
    ano = int(input(f'Ano de nascimento da pessoa {c}: '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'Dessas 7 pessoas {maior} são maiores de idade e {menor} são menores de idade.')