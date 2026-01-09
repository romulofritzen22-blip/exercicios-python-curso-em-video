#Desafio 008: Crie um programa que leia um valor em metros e o exiba convertido em milímetros e centímetros.
#(Posteriormente é proposto converter em algumas outras medidas.)

m = float(input('Digite um valor em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000

print(f'{m} metro(s) equivale a: \n{mm} milímetros \n{cm} centímetros \n{dm} decímetros \n{dam} decâmetros \n{hm} hectômetros \n{km} kilômetros')
