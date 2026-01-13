#Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#e em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase qualquer: ').strip().upper()

print(f'A letra "a" aparece {frase.count('A')} vezes.')
print(f'A primeira posição em que a letra "a" aparece é {(frase.find('A') + 1)}')
print(f'A última posição em que a letra "a" aparece é {(frase.rfind('A') + 1)}')
