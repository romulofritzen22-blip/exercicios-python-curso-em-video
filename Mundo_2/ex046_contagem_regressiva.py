#Desafio 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from emoji import emojize
from time import sleep

print('VIRADA DE ANO!!!')
for contagem in range(10, 0, -1):
    sleep(1)
    print(contagem)
sleep(1)
print(emojize(':fogos_de_artifício:', language='pt'))
