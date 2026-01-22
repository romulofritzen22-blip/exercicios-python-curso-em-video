#Desafio 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date
ano = int(input('Em que ano o atleta nasceu? '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Portanto ele está na categoria [ MIRIM ]')
elif idade <= 14:
    print('Portanto ele está na categoria [ INFANTIL ]')
elif idade <= 19:
    print('Portanto ele está na categoria [ JÚNIOR ]')
elif idade <= 25:
    print('Portanto ele está na categoria [ SÊNIOR ]')
else:
    print('Portanto ele está na categoria [ MASTER ]')
