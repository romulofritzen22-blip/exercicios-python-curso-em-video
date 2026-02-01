#Desafio 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos dessa PA são:')
for termos in range(primeiro_termo, primeiro_termo + razao * 10, razao):
    print(termos, end= '  ')
