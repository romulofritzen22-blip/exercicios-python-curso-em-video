#Desafio 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o nome da sua cidade: ').upper().strip().split()

print(f"A cidade começa com Santo? R= {'SANTO' in cidade[0]}")
