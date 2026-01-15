#Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano aleatório: '))

if (ano % 4 == 0 and not ano % 100 == 0) or (ano % 400 == 0):
    print(f'{ano} É um ano bissexto!')
else:
    print(f'{ano} NÃO É um ano bissexto.')
