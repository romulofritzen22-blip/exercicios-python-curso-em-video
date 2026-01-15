#Desafio 035: Desenvolva um programa que leia o comprimento de três retas.
#Diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Com essas retas é POSSÍVEL formar um triângulo.')
else:
    print('Com essas retas é IMPOSSÍVEL formar um triângulo.')
