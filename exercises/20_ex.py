# Make a Python program that opens and plays audio from an MP3 file.

import pygame

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
