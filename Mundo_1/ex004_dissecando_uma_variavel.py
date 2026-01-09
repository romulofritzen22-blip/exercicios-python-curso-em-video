#Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

texto = input('Digite algo a ser avaliado pelos métodos de string: ')

print(type(texto))

print('É alfanumérico? ', texto.isalnum())
print('É alfabético? ', texto.isalpha())
print('Está na tabela ASCII? ', texto.isascii())
print('É decimal? ', texto.isdecimal())
print('É dígito? ', texto.isdigit())
print('É numérico? ', texto.isnumeric())
print('Pode ser nome de variável? ', texto.isidentifier())
print('Está em minúsculas? ', texto.islower())
print('Está em maiúsculas? ', texto.isupper())
print('Está em formato de título? ', texto.istitle())
print('É espaço? ', texto.isspace())
print('É imprimível? ', texto.isprintable())
