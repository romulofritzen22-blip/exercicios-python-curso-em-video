#Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

m2 = largura * altura

print(f'A parede é de dimensão {largura:.2f} x {altura:.2f} com {m2:.2f} metros quadrados.')

tinta = m2 / 2
print(f'Para pintar essa parede você vai precisar de {tinta:.2f} l de tinta.')
