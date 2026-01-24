#Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#Abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#Entre 25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / altura ** 2
print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc < 25:
    print('Você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
