#Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print(f'{' JOKENPÔ ':=^30}')
usuario = int(input(f'1. Pedra \n2. Papel \n3. Tesoura \n{'=' * 30} \nOpção: '))
pc = randint(1, 3)

if usuario == pc:
    print('EMPATE!')
elif usuario == 1 and pc == 2:
    print('Você PERDEU! O computador escolheu PAPEL!')
elif usuario == 1 and pc == 3:
    print('Você VENCEU! O computador escolheu TESOURA!')
elif usuario == 2 and pc == 1:
    print('Você VENCEU! O computador escolheu PEDRA!')
elif usuario == 2 and pc == 3:
    print('Você PERDEU! O computador escolheu TESOURA!')
elif usuario == 3 and pc == 1:
    print('Você PERDEU! O computador escolheu PEDRA!')
elif usuario == 3 and pc == 2:
    print('Você VENCEU! O computador escolheu PAPEL!')
else:
    print('ERRO! Escolha uma opção válida!')
