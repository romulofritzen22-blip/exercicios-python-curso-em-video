#Desafio 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#O módulo playsound já está desatualizado há tempos.
#Por isso decidi usar o Nava, que é mais simples que o pygame.
#O Nava só funciona com arquivos ".wav", mas a lógica é a mesma do MP3.

import nava
nava.play("nirvana_in_bloom.wav")

# Obs: o arquivo "nirvana_in_bloom.wav" não está incluído no repositório.
# Para testar o código, coloque um arquivo .wav no mesmo diretório do script. 
