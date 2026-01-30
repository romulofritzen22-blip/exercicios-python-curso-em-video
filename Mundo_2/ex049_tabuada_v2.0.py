#Desafio 049: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

multiplicando = 0
multiplicador = int(input('===== TABUADA ===== \nDigite um número: '))

for produto in range (multiplicador, multiplicador * 11, multiplicador):
    multiplicando += 1
    print(f'{multiplicando} x {multiplicador} = {produto}')
