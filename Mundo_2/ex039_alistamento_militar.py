#Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 
#Se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
genero = int(input('Qual é o seu gênero? Digite: \n [1] Masculino \n [2] Feminino \n Genêro: '))

if genero == 2:
    print('Você não precisa fazer alistamento militar obrigatório.')
elif idade < 18:
    print(f'Você deve se alistar no exército daqui {18 - idade} ano(s), em {ano + 18}.')
elif idade == 18:
    print('Você deve se alistar no exército neste ano!')
else:
    print(f'Você deveria ter se alistado no exército há {idade - 18} ano(s) atrás, em {ano + 18}.')
