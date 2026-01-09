#Desafio 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto em centímetros: '))
ca = float(input('Comprimento do cateto adjacente em centímetros: '))

h = hypot(co, ca)

print(f'O comprimento da hipotenusa é de: {(h):.2f}cm')
