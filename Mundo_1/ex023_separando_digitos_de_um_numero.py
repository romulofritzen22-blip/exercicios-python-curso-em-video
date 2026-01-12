#Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.


#método de string (quebra se n < 1000):

n = input('Digite um número entre 0 e 9999: ').strip()

print(f'Seu número tem {n[3]} unidades.')
print(f'Seu número tem {n[2]} dezenas.')
print(f'Seu número tem {n[1]} centenas.')
print(f'Seu número tem {n[0]} milhares.')

#método matemático (mais recomendável):

n = int(input('Digite um número de 0 a 9999: '))

print(f'Seu número tem {n % 10} unidades.')
print(f'Seu número tem {n // 10 % 10} dezenas.')
print(f'Seu número tem {n // 100 % 10} centenas.')
print(f'Seu número tem {n // 1000 % 10} milhares.')
