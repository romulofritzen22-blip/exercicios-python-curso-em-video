#Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idades = []
mulheres_20 = 0
idade_velho = 0 
nome_velho = ''

for pessoa in range(1, 5):
    nome = input(f'Pessoa {pessoa}: \nNome: ')
    idade = int(input('Idade: '))
    genero = int(input('Gênero: \n( 1 ) Masculino \n( 2 ) Feminino \nSua opção: '))
    idades.append(idade)
    if genero == 2 and idade < 20:
        mulheres_20 += 1
    if genero == 1:
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome

print(f'A média de idade do grupo é de {sum(idades) / pessoa:.0f} anos.')
print(f'Nesse grupo {mulheres_20} mulher(es) tem menos de 20 anos.')
if nome_velho == '':
    print('Não existe nenhum homem no grupo.')
else:
    print(f'O homem mais velho do grupo é o {nome_velho}.')
