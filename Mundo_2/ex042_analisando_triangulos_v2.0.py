#Desafio 042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))

if not (a < b + c and b < a + c and c < a + b):
    print('Essas retas NÃO PODEM formar um triângulo.')
elif a == b == c:
    print('Essas retas podem formar um triângulo EQUILÁTERO.')
elif a == b or a == c or b == c:
    print('Essas retas podem formar um triângulo ISÓSCELES.')
else:
    print('Essas retas podem formar um triângulo ESCALENO.')
