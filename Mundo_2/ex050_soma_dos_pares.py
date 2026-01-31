#Desafio 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

pares = []
for c in range (1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        pares.append(num)
print(f'A soma de todos os números pares é {sum(pares)}')