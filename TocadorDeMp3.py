# importar a biblioteca pygame
from pygame import mixer

# uma forma de implementar o código
mixer.init()

# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3. Coloque o arquivo.mp3 na mesma pasta do arquivo.py
arquivo = input("Digite o nome do arquivo que deseja executar.")
mixer.music.load(f'{arquivo}.mp3')
mixer.music.play()
x = input('Digite algo para parar...')