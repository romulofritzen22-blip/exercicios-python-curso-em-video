#Desafio 019: Um professor quer sortear um dos seu quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')

print(f'O aluno escolhido para apagar o quadro é {choice([a1, a2, a3, a4])}.')
