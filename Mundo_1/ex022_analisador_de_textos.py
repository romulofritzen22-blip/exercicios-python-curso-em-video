#Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ').strip()

print(f'Seu nome completo em maiúsculas é: {nome.upper()}')
print(f'Seu nome completo em minúsculas é: {nome.lower()}')
print(f'Seu nome completo tem {len(nome) - nome.count(' ')} letras.')

lista_nomes = nome.split()
print(f'Seu primeiro nome é {lista_nomes[0]} e tem {len(lista_nomes[0])} letras.')
