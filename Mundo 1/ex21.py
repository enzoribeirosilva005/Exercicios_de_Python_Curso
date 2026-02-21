'''Abrindo um aúdio no Python'''

import pygame
import time

# Inicia o programa
pygame.mixer.init()

# Carrega o arquivo mp3
pygame.mixer.music.load(r'C:\Users\Rick\Downloads\audio_teste.mp3')

# Tocamos o arquivo
pygame.mixer.music.play()

print('Reproduzindo...')

# Aqui o programa continua rodando enquanto toca o mp3
while pygame.mixer.music.get_busy():
    time.sleep(1)