#Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
a = float(input('Digite um ângulo: '))
ar = radians(a)

print(f'O ângulo {a} tem seno de {sin(ar):.3f}, cosseno de {cos(ar):.3f} e tangente de {tan(ar):.3f}')
