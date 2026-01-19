#Desafio 037: Escreva um programa em Python que leia um número inteiro qualquer.
#Peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))

escolha = int(input('Digite: \n1 para converter em BINÁRIO \n2 para converter em OCTAL \n3 para converter em HEXADECIMAL\nSua escolha: '))

if escolha == 1:
    print(f'O número {num} em BINÁRIO é {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} em OCTAL é {oct(num)[2:]}')
elif escolha == 3:
    print(f'O número {num} em HEXADECIMAL é {hex(num)[2:]}')
else:
    print('ERRO! Digite um número entre 1 e 3!')