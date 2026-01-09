#Desafio 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))

a = numero - 1 
s = numero + 1

print(f'O antecessor de {numero} é {a} e o sucessor é {s}.')
