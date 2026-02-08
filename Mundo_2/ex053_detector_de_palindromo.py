#Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = (input('DETECTOR DE PALÍNDROMO: \nDigite uma frase: ')).lower().split()
frase = ''.join(frase)

if frase == frase[::-1]:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase NÃO é um palíndromo.')