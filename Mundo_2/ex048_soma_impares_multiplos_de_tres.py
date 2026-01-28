#Desafio 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

lista_multiplos_3 = []
for multiplos_3 in range(3, 501, 3):
    if multiplos_3 % 2 == 1:
        lista_multiplos_3.append(multiplos_3)
print(f'A soma dos multiplos de 3 ímpares entre 1 e 500 é {sum(lista_multiplos_3)}')
