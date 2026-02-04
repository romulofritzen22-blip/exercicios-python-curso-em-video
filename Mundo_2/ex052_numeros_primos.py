#Desafio 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

if num <= 1:
    print(f'O número {num} NÃO É PRIMO.')
else:
    divisivel = 0
    for c in range(1, num + 1):
        if num % c == 0:
            divisivel += 1
    if divisivel == 2:
        print(f'O número {num} É PRIMO.')
    else: 
        print(f'O número {num} NÃO É PRIMO.')
