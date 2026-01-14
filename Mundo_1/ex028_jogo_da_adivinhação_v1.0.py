#Desafio 028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5.
#Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
pc_num = randint(0, 5)
user_num = int(input('Estou pensando em um número entre 0 e 5, adivinhe qual é: '))

if user_num == pc_num:
    print('Acertou! :(')
else:
    print(f'Errou! Eu pensei em {pc_num} XD')
