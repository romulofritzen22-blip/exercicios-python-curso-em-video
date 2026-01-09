#Desafio 014: Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

tc = float(input('Digite uma temperatura em °C: '))
tf = tc * 1.8 + 32

print(f'A temperatura de {tc} °C equivale a {tf} °F.')
