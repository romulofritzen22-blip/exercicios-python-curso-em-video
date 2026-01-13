#Desafio 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite seu nome completo: ').strip().upper()
print(f'Você tem "Silva" no nome? R= {'SILVA' in nome}')
